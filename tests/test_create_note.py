import unittest
from campusflow.validate import validate_ticket_id, validate_message

class TestCreateNote(unittest.TestCase):

    def test_validate_ticket_id_success(self):
        self.assertEqual(validate_ticket_id(" TCK-101 "), "TCK-101")
        self.assertEqual(validate_ticket_id("NOTE-2026"), "NOTE-2026")

    def test_validate_ticket_id_empty_or_spaces(self):
        with self.assertRaises(ValueError):
            validate_ticket_id("   ")
        with self.assertRaises(ValueError):
            validate_ticket_id("")

    def test_validate_ticket_id_wrong_type(self):
        with self.assertRaises(ValueError):
            validate_ticket_id(123)


    def test_validate_message_success(self):
        valid_300_word_message = " ".join(["word"] * 300)
        
        result = validate_message("   " + valid_300_word_message + "   ")
        self.assertEqual(result, valid_300_word_message)

    def test_validate_message_empty(self):
        with self.assertRaises(ValueError):
            validate_message("       ")

    def test_validate_message_too_short(self):
        short_message = "This is a short message with only eight words."
        with self.assertRaises(ValueError):
            validate_message(short_message)

if __name__ == "__main__":
    unittest.main()
