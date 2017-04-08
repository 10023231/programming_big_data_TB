# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 16:31:05 2017

@author: Tanya
"""
#Tatiana Borta
#10023231

from calculator import *
import unittest
class MyTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(multiply(5, 3), 15)
        self.assertEqual(devide(6, 3),2)
        self.assertEqual(exponential(5, 3), 125)
        self.assertEqual(sqrt(25), 5)
        self.assertEqual(cube(3), 27)
        self.assertEqual(power(5), 25)
        self.assertEqual(sine(1000),  0.83)
        self.assertEqual(tangent(23), 1.59)
    def test_2(self):     
        self.assertEqual(add(2, 2), 4)
        self.assertEqual(subtract(2, 2), 0)
        self.assertEqual(multiply(2, 2), 4)
        self.assertEqual(devide(2, 2), 1)
        self.assertEqual(exponential(2, 2), 4)
        self.assertEqual(sqrt(100), 10)
        self.assertEqual(cube(6), 216)
        self.assertEqual(power(6), 36)
        self.assertEqual(sine(2000), 0.93)
        self.assertEqual(tangent(32), 0.66)
    def test_3(self):  
        self.assertEqual(add(4, 0), 4)
        self.assertEqual(subtract(4, 0), 4)
        self.assertEqual(subtract(4, 5), -1)
        self.assertEqual(multiply(4, 0), 0)
        self.assertEqual(devide(4, 0), 'undefined')
        self.assertEqual(exponential(4, 0), 1)
        self.assertEqual(sqrt(36), 6)
        self.assertEqual(cube(4), 64)
        self.assertEqual(power(7), 49)
        self.assertEqual(sine(3000), 0.22)
        self.assertEqual(tangent(35), 0.47)
if __name__ == '__main__':
     unittest.main() 