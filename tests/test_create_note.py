import unittest
from campusflow.validate import validate_ticket_id, validate_message

class TestCreateNote(unittest.TestCase):


    def test_validate_ticket_id_success(self):
        """Should clean surrounding spaces and return valid string IDs."""
        self.assertEqual(validate_ticket_id(" TCK-101 "), "TCK-101")
        self.assertEqual(validate_ticket_id("NOTE-2026"), "NOTE-2026")

    def test_validate_ticket_id_empty_or_spaces(self):
        """Should throw ValueError if the ID is blank or just spaces."""
        with self.assertRaises(ValueError):
            validate_ticket_id("   ")
        with self.assertRaises(ValueError):
            validate_ticket_id("")

    def test_validate_ticket_id_wrong_type(self):
        """Should throw ValueError if input is not a string."""
        with self.assertRaises(ValueError):
            validate_ticket_id(123)


    def test_validate_message_success(self):
        """Should validate and strip a message that meets the word requirement."""
        valid_300_word_message = " ".join(["word"] * 300)
        
        result = validate_message("   " + valid_300_word_message + "   ")
        self.assertEqual(result, valid_300_word_message)

    def test_validate_message_empty(self):
        """Should throw ValueError if the message body is empty."""
        with self.assertRaises(ValueError):
            validate_message("       ")

    def test_validate_message_too_short(self):
        """Should throw ValueError if the message has fewer than 300 words."""
        short_message = "This is a short message with only eight words."
        with self.assertRaises(ValueError):
            validate_message(short_message)

if __name__ == "__main__":
    unittest.main()
