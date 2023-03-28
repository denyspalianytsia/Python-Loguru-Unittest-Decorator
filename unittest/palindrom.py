import unittest

def palindrom(words):
    palindroms = ''.join(reversed(words))
    if words == palindroms:
        print("It is palindrom")
        return palindroms
    else:
        print("It is not palindrom")
        return palindroms

class Test_palindrom(unittest.TestCase):

    def test_palindrom(self):
        self.assertEqual(palindrom("mom"), "mom")
        self.assertEqual(palindrom("non non"), "non non")

if __name__ == "__main__":
    unittest.main()