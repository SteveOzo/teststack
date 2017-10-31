
import unittest
import picoplaca

class TestMyModule(unittest.TestCase):

    def test_can_road(self):
        test1 = picoplaca.Auto("PZC-566")
        self.assertEqual(test1.getIsPico("2017-11-01","15:00"), "Puede Circular") #Testing case Day="prohibited" Hour="Free"
        self.assertEqual(test1.getIsPico("2017-11-05","15:00"), "Puede Circular") #Testing case Day="Sunday" Hour="Free"
        self.assertEqual(test1.getIsPico("2017-11-06","8:00"), "Puede Circular") #Testing case Day="Free" Hour="prohibited"
        self.assertEqual(test1.getIsPico("2017-11-01","16:00"), "No Circula") #Testing case Day="prohibited" Hour="prohibited"

if __name__ == "__main__":
    unittest.main()
