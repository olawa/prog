
"""
Solutions to module 4
Review date:
"""

student = "Ola Wallerman"
reviewer = ""

import math as m
import random as r
import numpy as np
from functools import reduce


def sphere_volume(n, d):
    # n is a list of set of coordinates
    # d is the number of dimensions of the sphere 
    sum_squares = []
    for i in range(n):
        coords = []
        for j in range(d):
             coords.append(r.uniform(-1 , 1))
        squares = list((map(lambda x: x**2, coords)))
        sum_squares.append(reduce(lambda x, y: x + y, squares)) # replace  with built in sum for faster code      
        # sum_squares = sum(squares)
    inside = list(filter(lambda x: x <=1, sum_squares)) # replaces if sum_squares <= 1: inside +=1
   # print(2**d * len(inside)/n)
    return 2**d * len(inside)/n


def hypersphere_exact(n,d):
    return  m.pi ** (d/2) / m.gamma(d/2 + 1)
     
def main():
    n = 1000000
    d = 11
    sphere_volume(n,d)
    print(hypersphere_exact(n, d))


if __name__ == '__main__':
	main()
