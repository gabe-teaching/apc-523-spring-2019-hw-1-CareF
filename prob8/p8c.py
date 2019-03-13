#!/usr/bin/env python
# -*- coding:utf-8 -*-
from scipy.integrate import quad
from numpy import exp, e
k=20
N=31

if __name__ == "__main__":
    yk = quad(lambda x: x**k*exp(x), 0, 1)[0]
    y = [0]*N
    for n in reversed(range(k, N)):
        y[n-1] = (e - y[n])/n
    print("Numerical integratal: ", yk)
    print("Reversed recurrence: ", y[k])
    print("Error: %e"%abs(y[k]/yk-1))

# Output:
#  Numerical integratal:  0.12380383076256998
#  Reversed recurrence:  0.12380383076256918
#  Error: 6.550316e-15

