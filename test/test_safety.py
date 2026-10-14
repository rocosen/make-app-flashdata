"""Check publishable artifacts for credential leaks and unintended paid work.

These offline checks do not execute Make IML or replace platform scenario tests.
"""
import copy
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
APP = ROOT / 'app'
EXPECTED = {'google_search', 'google_news', 'google_images', 'google_shopping',
            'google_videos', 'google_places', 'youtube_search', 'youtube_search_extended',
            'youtube_metadata', 'youtube_transcript', 'youtube_captions',
            'youtube_trainability', 'youtube_channel', 'youtube_suggestions', 'youtube_download'}


def read(path):
    return json.loads((APP / path).read_text())


class SafetyContract(unittest.TestCase):
    def test_connection_verifies_without_submitting_work(self):
        c = read('connections/api-key/communication.json')
        self.assertEqual(c['url'], 'https://api.flashdata.dev/v2/api-access')
        self.assertEqual(c['method'], 'GET')
        self.assertNotIn('body', c)
        self.assertNotIn('qs', c)
        self.assertNotIn('metadata', c['response'])
        p = read('connections/api-key/parameters.json')[0]
        self.assertEqual(p['type'], 'password')
        self.assertNotIn('default', p)

    def test_authenticated_calls_configure_explicit_redirect_controls(self):
        for c in (read('base.json'), read('connections/api-key/communication.json')):
            self.assertIn('request.headers.x-api-key', c['log']['sanitize'])
            self.assertIn('x-api-key', c['headers'])
        connection = read('connections/api-key/communication.json')
        self.assertIs(connection['followRedirect'], False)
        self.assertIs(connection['followAllRedirect'], False)
        for p in (APP / 'modules').glob('*/communication.json'):
            data = json.loads(p.read_text())
            for c in data if isinstance(data, list) else [data]:
                self.assertIs(c.get('followRedirect'), False, str(p))
                self.assertIs(c.get('followAllRedirect'), False, str(p))
                self.assertNotIn('repeat', c)

    def test_paid_errors_keep_service_details_without_retry_type(self):
        e = read('base.json')['response']['error']
        self.assertEqual(e['type'], 'RuntimeError')
        self.assertIn('body.message', e['message'])
        self.assertIn('body.field', e['message'])
        for p in (APP / 'modules').glob('*/communication.json'):
            text = p.read_text()
            self.assertNotIn('RateLimitError', text)
            self.assertNotIn('ConnectionError', text)

    def test_fifteen_sources_have_distinct_task_scopes(self):
        cap = read('capabilities.json')
        self.assertEqual(set(cap), EXPECTED)
        self.assertEqual(len({v['name'] for v in cap.values()}), 15)
        for source, spec in cap.items():
            c = read('modules/' + spec['folder'] + '/communication.json')
            self.assertEqual(c['body']['source'], source)
            self.assertEqual(c['method'], 'POST')
            self.assertEqual(c['url'], '/v1/queries' if source == 'youtube_download' else '/v1/queries/realtime')
            self.assertNotIn('raw', c['response']['output'])

    def test_pagination_retains_query_and_has_an_explicit_paid_cap(self):
        for source, spec in read('capabilities.json').items():
            c = read('modules/' + spec['folder'] + '/communication.json')
            if not source.startswith('google_'):
                self.assertNotIn('pagination', c)
                continue
            first = copy.deepcopy(c['body'])
            page = copy.deepcopy(c['pagination']['body'])
            self.assertEqual(first['params'].pop('page'), 1)
            self.assertEqual(page['params'].pop('page'), '{{pagination.page}}')
            self.assertEqual(first, page)
            self.assertEqual(c['pagination']['condition'], '{{pagination.page <= ifempty(parameters.maxPages, 1)}}')
            fields = read('modules/' + spec['folder'] + '/expect.json')
            self.assertEqual(next(p for p in fields if p['name'] == 'maxPages')['default'], 1)
            self.assertEqual(fields[-1]['name'], 'limit')
            self.assertFalse(fields[-1].get('required', False))
            self.assertEqual(c['response']['limit'], '{{parameters.limit}}')

    def test_explicit_false_and_separate_caption_defaults(self):
        for folder, default in [('get-video-transcript', True), ('get-video-captions', False)]:
            c = read('modules/' + folder + '/communication.json')
            self.assertEqual(c['body']['params']['auto'], '{{parameters.auto}}')
            self.assertEqual(next(p for p in read('modules/' + folder + '/expect.json') if p['name'] == 'auto')['default'], default)
        c = read('modules/get-video-metadata/communication.json')
        self.assertEqual(c['body']['params']['include_formats'], '{{parameters.includeFormats}}')

    def test_universal_rejects_external_urls_and_sensitive_header_overrides(self):
        fields = read('modules/make-an-api-call/expect.json')
        path = next(p for p in fields if p['name'] == 'url')['validate']['pattern']
        for bad in ['https://evil.example/', '//evil.example/', '/\\evil.example/', '/@evil.example/', '/a?api_key=x', '/%2f%2fevil.example', '/v2/jobs/job_test/results', '/v2/bulk-jobs/bulk_test/results/1']:
            self.assertIsNone(re.fullmatch(path, bad), bad)
        self.assertIsNotNone(re.fullmatch(path, '/v2/api-access'))
        key = next(p for p in fields if p['name'] == 'headers')['spec'][0]['validate']['pattern']
        for bad in ['host', 'HOST', 'Host', 'X-API-KEY', 'x-api-key', 'Authorization', 'Cookie', 'Proxy-Authorization']:
            self.assertIsNone(re.fullmatch(key, bad), bad)
        self.assertIsNotNone(re.fullmatch(key, 'Content-Type'))
        url = read('modules/make-an-api-call/communication.json')['url']
        self.assertNotIn('{{parameters.api}}', url)
        self.assertIn("'https://api.flashdata.dev'", url)
        self.assertIn("'https://data.flashdata.dev'", url)

    def test_download_storage_is_private_and_optional_mode_settings_stay_unset(self):
        c = read('modules/download-video/communication.json')
        self.assertIn('request.body.params.storage', c['log']['sanitize'])
        fields = read('modules/download-video/expect.json')
        storage = next(p for p in fields if p['name'] == 'storage')
        self.assertTrue(storage['required'])
        options = next(p for p in storage['spec'] if p['name'] == 'storage_type')['options']
        for provider in options:
            for p in provider['nested']:
                if p['name'] in ['access_key', 'secret_key', 'sas_token']:
                    self.assertEqual(p['type'], 'password')
                    self.assertNotIn('default', p)
            self.assertEqual(any(p['name'] == 'service_account' for p in provider['nested']), provider['value'] == 'gcs')
        for name in ['videoQuality', 'audioQuality', 'audioLanguage', 'outputFormat']:
            self.assertNotIn('default', next(p for p in fields if p['name'] == name))

    def test_result_reader_is_blocked_before_redirect_until_runtime_is_verified(self):
        access, link, content = read('modules/get-job-result/communication.json')
        self.assertEqual(access['url'], 'https://api.flashdata.dev/v2/api-access')
        self.assertEqual(access['response']['valid']['condition'], '{{false}}')
        self.assertIn('temporarily disabled', access['response']['valid']['message'])
        self.assertIn("substring(headers.location, 0, length(temp.resultOrigin)) === temp.resultOrigin", link['response']['valid']['condition'])
        self.assertIn("substring(headers.location, length(temp.resultOrigin), length(temp.resultOrigin) + 1) === '/'", link['response']['valid']['condition'])
        self.assertEqual(content['headers'], '{{emptycollection}}')
        self.assertEqual(content['url'], '{{temp.resultUrl}}')
        for c in [access, link, content]:
            self.assertEqual(c['method'], 'GET')
            self.assertNotIn('body', c)
        self.assertIn('response.headers.location', link['log']['sanitize'])
        self.assertIn('request.url', content['log']['sanitize'])

    def test_templates_never_fan_out_into_paid_calls_or_include_credentials(self):
        tasks = json.loads((ROOT / 'examples/tasks.json').read_text())
        self.assertEqual({t['source'] for t in tasks}, EXPECTED)
        self.assertEqual(sum(len(t['queries']) for t in tasks), 30)
        for t in tasks:
            self.assertLessEqual(len(t['description']), 1500)
            self.assertLessEqual(len(t['scenarioDescription']), 240)
            self.assertEqual(t['documentation'], 'https://flashdata.dev/docs/sources/' + t['source'])
            bp = json.loads((ROOT / t['blueprint']).read_text())
            self.assertEqual(bp['flow'][0]['module'], 'app#flashdata-g6iv9y:' + t['module'])
            for m in bp['flow']:
                self.assertNotIn('__IMTCONN__', m['parameters'])
                self.assertNotIn('storage', m['mapper'])
                self.assertNotIn('apiKey', m['mapper'])
            self.assertEqual(len(bp['flow']), 3 if t['source'] == 'youtube_download' else 1)
            if t['source'] == 'youtube_download':
                self.assertEqual([m['module'].split(':')[1] for m in bp['flow'][1:]], ['getJobStatus', 'getJobResult'])
                self.assertEqual(bp['flow'][2]['filter']['conditions'][0][0]['b'], 'completed')


if __name__ == '__main__':
    unittest.main()
