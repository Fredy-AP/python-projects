from sympy import *
import numpy as np

x = Symbol('x')
y = x**12 + 1

yprime = y.diff(x)
print(yprime)