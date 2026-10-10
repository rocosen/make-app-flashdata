"""Guard credential destinations and paid-query behavior in deployable definitions."""

import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1] / "app"


def read(path):
    return json.loads((ROOT / path).read_text())


class SafetyContract(unittest.TestCase):
    def test_verification_cannot_charge_a_query(self):
        connection = read("connections/api-key/communication.json")
        self.assertEqual(connection["url"], "https://api.flashdata.dev/v2/api-access")
        self.assertEqual(connection["method"], "GET")
        self.assertNotIn("body", connection)
        self.assertNotIn("qs", connection)

    def test_credentials_are_masked_and_never_follow_redirects(self):
        for config in [read("base.json"), read("connections/api-key/communication.json")]:
            self.assertIs(config["followRedirect"], False)
            self.assertIs(config["followAllRedirect"], False)
            self.assertIn("request.headers.`X-API-Key`", config["log"]["sanitize"])
        self.assertEqual(read("base.json")["baseUrl"], "https://data.flashdata.dev")
        parameter = read("connections/api-key/parameters.json")[0]
        self.assertEqual(parameter["type"], "password")
        self.assertNotIn("default", parameter)

    def test_paid_http_errors_do_not_select_platform_retry_types(self):
        error = read("base.json")["response"]["error"]
        self.assertEqual(error["type"], "RuntimeError")
        for value in error.values():
            if isinstance(value, dict):
                self.assertEqual(value["type"], "RuntimeError")

    def test_paid_query_definitions_have_no_repeat_or_implicit_pagination(self):
        for file in (ROOT / "modules").glob("*/communication.json"):
            config = json.loads(file.read_text())
            self.assertIsInstance(config, dict)
            self.assertNotIn("repeat", config)
            self.assertNotIn("pagination", config)
            self.assertEqual(config["url"], "/v1/queries/realtime")
            self.assertEqual(config["method"], "POST")
            self.assertNotIn("headers", config)

    def test_explicit_false_does_not_get_replaced_with_default(self):
        body = read("modules/search-web-results/communication.json")["body"]
        self.assertEqual(body["params"]["autocorrect"], "{{parameters.autocorrect}}")
        self.assertEqual(body["params"]["num"], "{{parameters.limit}}")
        self.assertEqual(body["params"]["page"], "{{parameters.page}}")


if __name__ == "__main__":
    unittest.main()
