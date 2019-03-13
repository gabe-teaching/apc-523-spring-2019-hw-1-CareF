#!/usr/bin/env python
# -*- coding:utf-8 -*-
import numpy as np
from numpy.polynomial.polynomial import Polynomial
N = 20
a = [0]*(N+1)
def prods(N, n=0, prod=1):
    if N == 0:
        a[n] += prod
        return
    prods(N-1, n+1, prod*N)
    prods(N-1, n, prod)

if __name__ == "__main__":
    prods(N)
    coef = [a[n]*(-1)**(N-n) for n in range(len(a))]
    print(np.array(coef))

    from functools import reduce
    print(np.array([reduce(lambda a, b: a*x+b, coef)
                    for x in range(1, 21)]))
    print(np.array([reduce(lambda a, b: a*x*1.0+b, coef)
                    for x in range(1, 21)]))
    coef.reverse()
    w = Polynomial(np.array(coef, dtype=np.float))
    # have to explicitly specify dtype, 
    # otherwise root finder doesn't work
    print([w(x) for x in range(1, 21)])
    print(w.roots()) 
    # This uses eigenvalues of the companion matrix for roots
    from scipy.optimize import root
    print(root(w, 21.0))
    # This uses Optimization method root finding
    for delta in (1e-8, 1e-6, 1e-4, 1e-2):
        coef[20] = 1 + delta
        w = Polynomial(np.array(coef, dtype=np.float))
        print(root(w, 21.0))
    coef[20]=1
    coef[19]=-210-2**(-23)
    w = Polynomial(np.array(coef, dtype=np.float))
    print(root(w, 16.1))
    print(root(w, 17.1))
    print(w.roots())
    coef[19]=-210
    w = Polynomial(np.array(coef, dtype=np.float))
    wp = w.deriv()
    [print("%g"%(sum(
        [abs(coef[l])*k**(l-1) for l in range(len(coef))])/abs(wp(k))))
     for k in (14, 16,17, 20)]
