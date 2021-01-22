import unittest
import n2w

# These test cases should provide a code coverage of 100%, unless I've missed something.

class TestNumToWords(unittest.TestCase):
    def test_num_to_words(self):
        self.assertRaises(ValueError, n2w.num_to_words, -500)
        self.assertRaises(ValueError, n2w.num_to_words, 1000000)
        self.assertRaises(ValueError, n2w.num_to_words, 'Rs. Two Thousand ONLY')
        self.assertEqual(n2w.num_to_words(0), 'Rs. Zero ONLY')
        self.assertEqual(n2w.num_to_words(7), 'Rs. Seven ONLY')
        self.assertEqual(n2w.num_to_words(19), 'Rs. Nineteen ONLY')
        self.assertEqual(n2w.num_to_words(69), 'Rs. Sixty-Nine ONLY')
        self.assertEqual(n2w.num_to_words(200), 'Rs. Two Hundred ONLY')
        self.assertEqual(n2w.num_to_words(217), 'Rs. Two Hundred And Seventeen ONLY')
        self.assertEqual(n2w.num_to_words(345), 'Rs. Three Hundred And Forty-Five ONLY')
        self.assertEqual(n2w.num_to_words(701), 'Rs. Seven Hundred And One ONLY')
        self.assertEqual(n2w.num_to_words(3000), 'Rs. Three Thousand ONLY')
        self.assertEqual(n2w.num_to_words(4007), 'Rs. Four Thousand Seven ONLY')
        self.assertEqual(n2w.num_to_words(6045), 'Rs. Six Thousand Forty-Five ONLY')
        self.assertEqual(n2w.num_to_words(9999), 'Rs. Nine Thousand Nine Hundred And Ninety-Nine ONLY')
        self.assertEqual(n2w.num_to_words(10001), 'Rs. Ten Thousand One ONLY')
        self.assertEqual(n2w.num_to_words(10019), 'Rs. Ten Thousand Nineteen ONLY')
        self.assertEqual(n2w.num_to_words(11124), 'Rs. Eleven Thousand One Hundred And Twenty-Four ONLY')
        self.assertEqual(n2w.num_to_words(30789), 'Rs. Thirty Thousand Seven Hundred And Eighty-Nine ONLY')
        self.assertEqual(n2w.num_to_words(50000), 'Rs. Fifty Thousand ONLY')
        self.assertEqual(n2w.num_to_words(100000), 'Rs. One Lakh ONLY')
        self.assertEqual(n2w.num_to_words(100001), 'Rs. One Lakh One ONLY')
        self.assertEqual(n2w.num_to_words(100019), 'Rs. One Lakh Nineteen ONLY')
        self.assertEqual(n2w.num_to_words(100378), 'Rs. One Lakh Three Hundred And Seventy-Eight ONLY')
        self.assertEqual(n2w.num_to_words(605656), 'Rs. Six Lakh Five Thousand Six Hundred And Fifty-Six ONLY')
        self.assertEqual(n2w.num_to_words(705006), 'Rs. Seven Lakh Five Thousand Six ONLY')
        self.assertEqual(n2w.num_to_words(123456.78), 'Rs. One Lakh Twenty Three Thousand Four Hundred And Fifty-Six 78/100 ONLY')
        self.assertEqual(n2w.num_to_words(797979.01), 'Rs. Seven Lakh Ninety Seven Thousand Nine Hundred And Seventy-Nine 1/100 ONLY')
        self.assertEqual(n2w.num_to_words(797979.10), 'Rs. Seven Lakh Ninety Seven Thousand Nine Hundred And Seventy-Nine 10/100 ONLY')
        self.assertEqual(n2w.num_to_words(999999.00), 'Rs. Nine Lakh Ninety Nine Thousand Nine Hundred And Ninety-Nine ONLY')
        self.assertEqual(n2w.num_to_words(999999.98), 'Rs. Nine Lakh Ninety Nine Thousand Nine Hundred And Ninety-Nine 98/100 ONLY')
        self.assertEqual(n2w.num_to_words(999999.99), 'Rs. Nine Lakh Ninety Nine Thousand Nine Hundred And Ninety-Nine 99/100 ONLY')

if __name__ == '__main__':
    unittest.main() # Allow us to run this file directly instead of running it through the unittest module.
