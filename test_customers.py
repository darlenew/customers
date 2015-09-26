#!/usr/bin/env python
from customers import Point, Customer, distance, load_json, invited

import unittest
class TestDistance(unittest.TestCase):
    santa_clara = Point(37.354444, -121.969167)
    san_francisco = Point(37.783333, -122.416667)

    def test_distance(self):
        # check for expected distance
        self.assertEqual("%.2f" % distance(self.santa_clara, self.san_francisco),
                         "%.2f" % 61.8861907035) # km
    
    def test_distance_zero(self):
        # check that distance between 2 equal points is 0
        self.assertEqual(distance(self.santa_clara, self.santa_clara),
                         0)
    
class TestLoadData(unittest.TestCase):
    def test_load_json(self):
        PATH = 'customers.txt'
        
        # expect 32 customers
        self.assertEqual(len(load_json(PATH)), 32)

class TestCustomers(unittest.TestCase):
    santa_clara = Point(37.354444, -121.969167)
    san_francisco = Point(37.783333, -122.416667)
    los_angeles = Point(34.05, -118.25)
    dublin = Point(53.3381985, -6.2592576)

    def setUp(self):
        c1 = Customer(1, name='Santa Clara', point=self.santa_clara)
        c2 = Customer(2, name='San Francisco', point=self.san_francisco)
        c3 = Customer(3, name='Los Angeles', point=self.los_angeles)
        c4 = Customer(4, name='Dublin', point=self.dublin)
        self.customers = [c1, c2, c3, c4]
                     
    def test_invited_within_500(self):
        result = invited(self.customers, self.santa_clara, 500)
        self.assertEqual(len(result), 3)

        result = invited(self.customers, self.dublin, 500)
        self.assertEqual(len(result), 1)

    def test_invited_within_zero(self):
        result = invited(self.customers, self.santa_clara, 0)
        self.assertEqual(len(result), 0)


if __name__ == "__main__":
    unittest.main()
