
"""
Solutions to module 4
Review date:
"""

student = "Ola Wallerman"
reviewer = ""

import math as m
import random as r
from functools import reduce

import concurrent.futures as future
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import wait
from time import perf_counter as pc


def sphere_volume(n, d):
    # n is a list of set of coordinates
    # d is the number of dimensions of the sphere 
    sum_squares = []
    for i in range(n):
        coords = []
        for j in range(d):
             coords.append(r.uniform(-1 , 1))
        squares = list((map(lambda x: x**2, coords)))   
        sum_squares.append(reduce(lambda x, y: x + y, squares))# replace reduce with built in sum for faster code      
    inside = list(filter(lambda x: x <=1, sum_squares))
    print(2**d * len(inside)/n)
    return 2**d * len(inside)/n

    return  

def hypersphere_exact(n,d):
    return

# parallel code - parallelize for loop
def sphere_volume_parallel1(n,d,np):
     #using multiprocessor to perform 10 iterations of volume function  
  #  executor = ProcessPoolExecutor(max_workers=np)
  #  futures =[]
  #  for y in range (10):
  #      futures.append(executor.submit(sphere_volume, n, d))
  #  wait(futures)
    sum = 0
    with future.ProcessPoolExecutor() as ex:
        for result in ex.map(sphere_volume, [n]*np, [d]*np):
             sum += result
 #       futures = [ex.submit(sphere_volume, n, d) for _ in range(np)]
 #   wait(futures)
 #   sum = 0
 #   for task in futures:
 #       sum += task.result()
 #   print()
    return sum / np
#sum(futures)/np


# parallel code - parallelize actual computations by splitting data
def sphere_volume_parallel2(n,d,np):
    executor = ProcessPoolExecutor(max_workers=np)
    new_n = n // np

    with future.ProcessPoolExecutor() as ex:
        futures = [ex.submit(sphere_volume, new_n, d) for _ in range(np)]
    wait(futures)

    sum = 0
    for task in futures:
        sum += task.result()
    print()
    return sum / np
    


def main():
    # part 1 -- parallelization of a for loop among 10 processes 
    n = 100000
    d = 11
    start = pc()
    # part 1 : parallell execution
   # executor = ProcessPoolExecutor(max_workers=np)
   # futures =[]
   # for y in range (10):
   #     futures.append(executor.submit(sphere_volume, n, d))
   # wait(futures)
    
    print(sphere_volume_parallel1(n, d, 10))
   
    stop = pc()
    print("Elapsed time:", stop - start) 


if __name__ == '__main__':
	main()
