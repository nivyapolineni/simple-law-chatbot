import unittest
import os
import json
from copilot.handlers import handle_matter_management, MATTERS_FILE

class TestMatterManagement(unittest.TestCase):

    def setUp(self):
        if os.path.exists(MATTERS_FILE):
            os.remove(MATTERS_FILE)

    def tearDown(self):
        if os.path.exists(MATTERS_FILE):
            os.remove(MATTERS_FILE)

    def test_create_matter(self):
        result = handle_matter_management("create matter Property Dispute with details Tenant not paying rent")
        self.assertEqual(result["action"], "CREATE")
        self.assertEqual(result["matter"]["name"], "Property Dispute")
        self.assertEqual(result["matter"]["details"], "Tenant not paying rent")

    def test_open_matter(self):
        handle_matter_management("create matter Divorce Case with details Mutual consent")
        result = handle_matter_management("open matter Divorce Case")
        self.assertEqual(result["action"], "OPEN")
        self.assertEqual(result["matter"]["name"], "Divorce Case")
        self.assertEqual(result["matter"]["details"], "Mutual consent")

    def test_open_nonexistent_matter(self):
        result = handle_matter_management("open matter Unknown Case")
        self.assertEqual(result["action"], "ERROR")
        self.assertIn("not found", result["message"])

if __name__ == "__main__":
    unittest.main()
