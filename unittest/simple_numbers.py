import unittest

def simle_numbers(num):
    if num > 1: 
        for i in range(2, num-1): 
            if (num%i) == 0: 
                print("Число є простим !") 
                return 1
                break 
            else: 
                print("Число не є простим числом") 
                return 0
                break
    else: 
        print("Число не є простим!")
        return 0

class Test_simple_numbers(unittest.TestCase):
    def test_simple_numbers(self):
        self.assertEqual(simle_numbers(1), 0)
        self.assertEqual(simle_numbers(11), 0)
        self.assertEqual(simle_numbers(10), 1)
        self.assertEqual(simle_numbers(124), 1)


if __name__ == "__main__":
    unittest.main()