import unittest
from my_tests_code.alterchar import alternatingCharacters


class TestAlternatingCharacters(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(alternatingCharacters(""), 0)

    def test_single_character(self):
        self.assertEqual(alternatingCharacters("A"), 0)
        self.assertEqual(alternatingCharacters("B"), 0)

    def test_all_same_characters(self):
        self.assertEqual(alternatingCharacters("AAAA"), 3)
        self.assertEqual(alternatingCharacters("BBBB"), 3)

    def test_alternating_characters(self):
        self.assertEqual(alternatingCharacters("ABABAB"), 0)
        self.assertEqual(alternatingCharacters("BABABA"), 0)

    def test_mixed_characters(self):
        self.assertEqual(alternatingCharacters("AABBAABB"), 4)
        self.assertEqual(alternatingCharacters("ABABAA"), 1)
        self.assertEqual(alternatingCharacters("BBABBA"), 2)
        self.assertEqual(alternatingCharacters("AAABBB"),4)


if __name__ == '__main__':
    unittest.main()