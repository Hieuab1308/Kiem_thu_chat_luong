import unittest
from main import analyze_numbers  # giả sử file bạn là analyzer.py

class TestAnalyzeNumbers(unittest.TestCase):
    def test_all_even(self):
        self.assertEqual(
            analyze_numbers([2, 4]),
            "2 là số chẵn\n4 là số chẵn"
        )

    def test_all_odd(self):
        self.assertEqual(
            analyze_numbers([1, 3]),
            "1 là số lẻ\n3 là số lẻ"
        )

    def test_mixed(self):
        self.assertEqual(
            analyze_numbers([1, 2]),
            "1 là số lẻ\n2 là số chẵn"
        )

    def test_empty(self):
        self.assertEqual(analyze_numbers([]), "")

if __name__ == "__main__":
    unittest.main()
