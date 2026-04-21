import unittest
from copilot.detector import detect_task, is_simple_explanation_requested
from copilot.handlers import handle_legal_qa
from copilot.formatter import format_output

class TestLegalCopilot(unittest.TestCase):

    def test_detection_contract(self):
        self.assertEqual(detect_task("This is a rental agreement"), "CONTRACT ANALYSIS")
        self.assertEqual(detect_task("NDA between parties"), "CONTRACT ANALYSIS")

    def test_detection_qa(self):
        self.assertEqual(detect_task("What is Section 420?"), "LEGAL Q&A")
        self.assertEqual(detect_task("Explain theft"), "LEGAL Q&A")

    def test_detection_drafting(self):
        self.assertEqual(detect_task("Draft a notice for eviction"), "LEGAL DRAFTING")
        self.assertEqual(detect_task("Write a legal notice"), "LEGAL DRAFTING")

    def test_simple_explanation_request(self):
        self.assertTrue(is_simple_explanation_requested("Explain this with a simple explanation"))
        self.assertFalse(is_simple_explanation_requested("Just explain this"))

    def test_handler_qa_uncertain(self):
        result = handle_legal_qa("What is the law regarding Martian travel?")
        self.assertIn("I am not certain", result["Explanation"])

    def test_formatter_unknown(self):
        output = format_output("UNKNOWN", None)
        self.assertIn("I am not certain", output)
        self.assertIn("Disclaimer", output)

if __name__ == "__main__":
    unittest.main()
