import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
       askPrice = float(quote['top_ask']['price'])
       bidPrice = float(quote['top_bid']['price'])
       returnedPrice = getDataPoint(quote)
       self.assertEqual((askPrice + bidPrice) / 2, returnedPrice[-1],"Calculate price test passed!")

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    returnedPrice = getDataPoint(quotes[0])   
    self.assertGreater(returnedPrice[1], returnedPrice[2], "Greater bid price than ask price")
        

  """ ------------ Add more unit tests ------------ """

  def test_calculateRatio(self): # getDataPoint method returns tuple 
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    
    self.assertEqual(
      getDataPoint(quotes[0])[-1] / getDataPoint(quotes[1])[-1],
      ((quotes[0]['top_bid']['price'] + quotes[0]['top_ask']['price']) / 2) / ((quotes[1]['top_bid']['price'] + quotes[1]['top_ask']['price']) / 2)
    )
      


  def test_calculatePriceReturnType(self): # getDataPoint method returns tuple 
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    for quote in quotes:
      self.assertIsInstance(getDataPoint(quote), tuple, "getDataPoint returned tuple")

  

  def test_calculateRationRaisesZeroDivisionError(self): #test the getRatio function raising error when second stock calculated price is 0
    quotes = [
      {'top_ask': {'price': 0, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 0, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    ABC = getDataPoint(quotes[0])[-1]
    DEF = getDataPoint(quotes[1])[-1]
    with self.assertRaises(ZeroDivisionError):
      getRatio(ABC, DEF)
           
    
    


if __name__ == '__main__':
    unittest.main()
