import unittest
from main import analyze_room_usage


class TestRoomUsage(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(analyze_room_usage([]), {})

    def test_single_room(self):
        lessons = [{"room": "101", "date": "2023-10-01", "time": "08:30"}]
        self.assertEqual(analyze_room_usage(lessons), {"101": 1})

    def test_multiple_rooms(self):
        lessons = [
            {"room": "101", "date": "2023-10-01", "time": "08:30"},
            {"room": "102", "date": "2023-10-01", "time": "10:00"},
            {"room": "101", "date": "2023-10-02", "time": "08:30"},
            {"room": "205", "date": "2023-10-02", "time": "10:00"},
        ]
        self.assertEqual(analyze_room_usage(lessons), {"101": 2, "102": 1, "205": 1})

    def test_missing_room_key(self):
        lessons = [{"date": "2023-10-01", "time": "08:30"}]
        self.assertEqual(analyze_room_usage(lessons), {})


if __name__ == "__main__":
    unittest.main()
