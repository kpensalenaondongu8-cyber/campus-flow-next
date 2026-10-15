import unittest

from campusflow.tickets import (
    create_ticket  
)

class TestCreateTicket(unittest.TestCase):
    def test_creates_ticket_with_all_fields(self):
        tickets = []
        ticket = create_ticket(tickets, "Wi-Fi down", "network", "HIGH", 15)
        self.assertEqual(
            ticket,
            {
                "id": "T001",
                "title": "Wi-Fi down",
                "category": "Network",
                "urgency": "high",
                "affected_users": 15,
                "priority": "critical",
                "status": "open",
                "assigned_to": None,
            },
        )

    def test_ticket_is_added_to_list(self):
        tickets = []
        ticket = create_ticket(tickets, "Broken laptop", "Hardware", "low", 1)
        self.assertEqual(tickets, [ticket])

    def test_priority_is_calculated_not_supplied(self):
        tickets = []
        ticket = create_ticket(tickets, "Slow portal", "Software", "low", 4)
        self.assertEqual(ticket["priority"], "medium")

    def test_new_ticket_starts_open_and_unassigned(self):
        ticket = create_ticket([], "Printer jam", "Other", "low", 1)
        self.assertEqual(ticket["status"], "open")
        self.assertIsNone(ticket["assigned_to"])

    def test_ids_are_sequential(self):
        tickets = []
        create_ticket(tickets, "First", "Other", "low", 1)
        second = create_ticket(tickets, "Second", "Other", "low", 1)
        self.assertEqual(second["id"], "T002")

    def test_id_continues_from_existing_tickets(self):
        tickets = [{"id": "T001"}, {"id": "T005"}]
        ticket = create_ticket(tickets, "Next", "Other", "low", 1)
        self.assertEqual(ticket["id"], "T006")

    def test_invalid_input_does_not_change_ticket_list(self):
        tickets = []
        create_ticket(tickets, "Valid", "Other", "low", 1)
        before = [dict(t) for t in tickets]

        with self.assertRaises(ValueError):
            create_ticket(tickets, "", "Other", "low", 1)
        with self.assertRaises(ValueError):
            create_ticket(tickets, "Bad users", "Other", "low", 0)
        with self.assertRaises(ValueError):
            create_ticket(tickets, "Bad urgency", "Other", "urgent", 1)
        with self.assertRaises(ValueError):
            create_ticket(tickets, "Bad category", "Plumbing", "low", 1)

        self.assertEqual(tickets, before)


if __name__ == "__main__":
    unittest.main()