# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 16:31:55 2017

@author: Tanya
"""
#Tatiana Borta
#10023231
import math
def add(num1, num2):#add two numbers
    return num1 + num2
def subtract(num1, num2):#substract two numbers
    return num1 - num2
def multiply(num1, num2):#multiplying two numbers
    return num1 * float(num2)
def devide(num1, num2):#devide two numbers
    if num2 == 0:
        return 'undefined'
    return num1 / float(num2)
def exponential(num1, num2): #exponential
    return num1 ** float(num2)
def sqrt(num1): #square root
    return num1 ** (1/2.0)
def cube(num1): #cube
    return num1 ** 3
def power(num1): #cube
    return num1 ** 2
def sine(num1): #sine
    answer = math.sin(num1)
    return round(answer, 2)
def tangent(num1): #tangent
    answer = math.tan(num1)
    return round(answer, 2)