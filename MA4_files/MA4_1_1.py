
"""
Solutions to module 4
Review date:
"""

student = "Ola Wallerman"
reviewer = ""


import random as r
import math as m
import matplotlib as mpl
mpl.use('tkagg')
import matplotlib.pyplot as plt 

def approximate_pi(n):
    x_outside = []
    y_outside = []
    x_inside = []
    y_inside = []
    for i in range(n):
        x = r.uniform(-1 , 1)
        y = r.uniform(-1 , 1)
        if (x**2 + y**2) > 1:
            x_outside.append(x)
            y_outside.append(y)
        else:
            x_inside.append(x)
            y_inside.append(y)
    my_pi = 4 * (len(x_inside)/n)
    plt.scatter(x_inside, y_inside, color = 'red', s = 1)
    plt.scatter(x_outside, y_outside, color = 'blue', s = 1)
    plt.title(f'{n} points, pi ~ {my_pi}')
    plt.savefig(f'pi-dots{n}.png')
    print(f'(Estimated pi to {my_pi} using n random poits (pi = {m.pi})')
    return my_pi

    return
    
def main():
    dots = [1000, 10000, 100000, 1000000]
    for n in dots:
        pi = approximate_pi(n)
       # print(pi)
       

if __name__ == '__main__':
	main()
