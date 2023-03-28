import unittest

def line_words(line):
    words = line.split()
    return words

class Test_line_words(unittest.TestCase):

    def test_line_words(self):
        self.assertEqual(line_words("Hello world!"), ["Hello", "world!"])
        self.assertEqual(line_words(" "), [])
        self.assertEqual(line_words("This unittest verifies the accuracy of the completed work"), ["This", "unittest", "verifies", "the", "accuracy", "of", "the", "completed", "work"])

if __name__ == "__main__":
    unittest.main()