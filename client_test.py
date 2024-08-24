import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):

    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        # Calculate expected prices
        expected_outputs = [
            ('ABC', 120.48, 121.2, (120.48 + 121.2) / 2),  # (120.48 + 121.2) / 2 = 120.84
            ('DEF', 117.87, 121.68, (117.87 + 121.68) / 2)  # (117.87 + 121.68) / 2 = 119.775
        ]

        for quote, expected in zip(quotes, expected_outputs):
            stock, bid_price, ask_price, price = getDataPoint(quote)
            self.assertEqual(stock, expected[0])
            self.assertEqual(bid_price, expected[1])
            self.assertEqual(ask_price, expected[2])
            self.assertAlmostEqual(price, expected[3], places=2)  # Match actual precision

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        # Calculate expected prices
        expected_outputs = [
            ('ABC', 120.48, 119.2, (120.48 + 119.2) / 2),  # (120.48 + 119.2) / 2 = 119.84
            ('DEF', 117.87, 121.68, (117.87 + 121.68) / 2)  # (117.87 + 121.68) / 2 = 119.775
        ]

        for quote, expected in zip(quotes, expected_outputs):
            stock, bid_price, ask_price, price = getDataPoint(quote)
            self.assertEqual(stock, expected[0])
            self.assertEqual(bid_price, expected[1])
            self.assertEqual(ask_price, expected[2])
            self.assertAlmostEqual(price, expected[3], places=2)  # Match actual precision

    def test_getRatio(self):
        prices = {
            'ABC': 120.84,
            'DEF': 119.77
        }
        expected_ratio = prices['ABC'] / prices['DEF']

        self.assertAlmostEqual(getRatio(prices['ABC'], prices['DEF']), expected_ratio, places=3)

    def test_getRatio_zero_price(self):
        prices = {
            'ABC': 120.84,
            'DEF': 0
        }

        with self.assertRaises(ZeroDivisionError):
            getRatio(prices['ABC'], prices['DEF'])

if __name__ == '__main__':
    unittest.main()