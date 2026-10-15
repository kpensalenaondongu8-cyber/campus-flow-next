import unittest
from campusflow.search import search_tickets

class TestSearchAndFiltering(unittest.TestCase):
    def setUp(self):
        self.tickets = [
            {"id": "T001", "title": "Wi-Fi router down", "category": "Network", "status": "open", "priority": "high"},
            {"id": "T002", "title": "Printer jammed", "category": "Hardware", "status": "in_progress", "priority": "medium"},
            {"id": "T003", "title": "Wi-Fi login error", "category": "Network", "status": "resolved", "priority": "low"},
        ]

    def test_case_insensitive_substring_search(self):
        results = search_tickets(self.tickets, query="WI-FI")
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0]["id"], "T001")
        self.assertEqual(results[1]["id"], "T003")

    def test_combined_filters_logical_and(self):
        # Updated query to match the hyphenation in "Wi-Fi"
        results = search_tickets(self.tickets, query="wi-fi", category="Network", status="open")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["id"], "T001")

    def test_empty_search_returns_all(self):
        results = search_tickets(self.tickets)
        self.assertEqual(len(results), 3)

    def test_no_match_returns_empty(self):
        results = search_tickets(self.tickets, query="nonexistent")
        self.assertEqual(len(results), 0)

if __name__ == "__main__":
    unittest.main()