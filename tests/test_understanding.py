import unittest
from campusflow.understanding_check import QUESTIONS

class TestUnderstandingCheck(unittest.TestCase):
    def test_question_bank_structure(self):
        self.assertEqual(len(QUESTIONS), 6)
        for q in QUESTIONS:
            self.assertIn("id", q)
            self.assertIn("prompt", q)
            self.assertIn("options", q)
            self.assertIn("answer", q)
            self.assertIn(q["answer"], q["options"])

if __name__ == "__main__":
    unittest.main()