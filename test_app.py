import unittest
import json

class ApiResponseTests(unittest.TestCase):
    def test_response_is_valid_json(self):
        response = {
            "message": "Hello from Compose!",
            "visits": 1
        }

        serialized = json.dumps(response)
        parsed = json.loads(serialized)

        self.assertEqual(parsed["message"], "Hello from Compose!")
        self.assertEqual(parsed["visits"], 1)

if __name__ == "__main__":
    unittest.main()
