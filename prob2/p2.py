#!/usr/bin/env python
# -*- coding:utf-8 -*-
from functools import reduce
from math import log10, ceil, factorial, exp
from operator import mul, add
class FiniteDicimal(object):
    def __init__(self, n=5, num=None):
        self.N = n
        self.digits = [0]*n
        self.exp = 0
        self.sign = 1
        if num:
            self.set(num)

    def value(self):
        return self.sign * 10**(self.exp-1) * reduce(
            lambda x, y: x/10.0+y, self.digits)

    def set(self, num):
        if num < 0:
            self.sign = -1
            num = -num
        self.exp = ceil(log10(num) + 1e-10)
        num = round(num/10**(self.exp-self.N))
        for n in range(self.N):
            self.digits[n] = num % 10
            num = num//10

    def __add__(self, num):
        return FiniteDicimal(self.N, self.value() + num.value())

    def __sub__(self, num):
        return FiniteDicimal(self.N, self.value() - num.value())

    def __mul__(self, num):
        return FiniteDicimal(self.N, self.value() * num.value())

    def __truediv__(self, num):
        return FiniteDicimal(self.N, self.value() / num.value())

    def __pow__(self, exp):
        if exp == 0:
            return FiniteDicimal(num=1)
        return self.__pow__(exp-1)*self

    def __eq__(self, num):
        return self.exp == num.exp and self.digits == num.digits

    def __neg__(self):
        return FiniteDicimal(self.N, -self.value())

    def __repr__(self):
        res = "0." if self.sign > 0 else "-0."
        for n in reversed(self.digits):
            res += str(n)
        return res + "e" + str(self.exp)

def fct(num):
    if num == 0:
        return FiniteDicimal(num=1)
    return FiniteDicimal(num=num)*fct(num-1)

if __name__ == "__main__":
    x = FiniteDicimal(num=5.5)
    terms = [x**n/fct(n) for n in range(31)]
    print("(a) ", terms)

    print("(b)")
    tot = FiniteDicimal()
    for n, s in enumerate(terms):
        tot += s
        print(n, tot, end="\t")
    trueValue = exp(5.5)
    print("Double:", trueValue, "Error", tot.value()/trueValue-1)

    tot = FiniteDicimal()
    for s in reversed(terms):
        tot += s
    trueValue = exp(5.5)
    print("(c)", tot, "Error", tot.value()/trueValue-1)
    e55 = tot

    trueValue = exp(-5.5)
    print("(d) Double:", trueValue)
    terms = [-t if n%2 else t for n, t in enumerate(terms)]
    tot = FiniteDicimal()
    print("(d.i)")
    for n, s in enumerate(terms):
        totnew = tot + s
        if totnew == tot:
            print("\nConverge at k=%d"%(n-1))
            break
        tot = totnew
        print(n, tot, end="\t")
    print(tot, "Error", abs(tot.value()/trueValue-1))

    print("(d.ii)")
    tot = FiniteDicimal()
    for n in range(1, 31):
        totnew = reduce(add, reversed(terms[:n]))
        if totnew == tot:
            print("\nConverge at k=%d"%(n-1))
            break
        tot = totnew
        print(n, tot, end="\t")
    print(tot, "Error", abs(tot.value()/trueValue-1))

    print("(d.iii)")
    tot = FiniteDicimal()
    for n in range(2, 31):
        totpositive = reduce(add, terms[0:n:2])
        totnegtive = reduce(add, terms[1:n:2])
        totnew = totpositive + totnegtive
        if totnew == tot:
            print("\nConverge at k=%d"%(n-1))
            break
        tot = totnew
        print(n, tot, end="\t")
    print(tot, "Error", abs(tot.value()/trueValue-1))

    print("(d.iv)")
    tot = FiniteDicimal()
    for n in range(2, 31):
        totpositive = reduce(add, reversed(terms[0:n:2]))
        totnegtive = reduce(add, reversed(terms[1:n:2]))
        totnew = totpositive + totnegtive
        if totnew == tot:
            print("\nConverge at k=%d"%(n-1))
            break
        tot = totnew
        print(n, tot, end="\t")
    print(tot, "Error", abs(tot.value()/trueValue-1))

    print("(e.i)")
    tot = FiniteDicimal()
    pairs = [terms[i] + terms[i+1] for i in range(0, 30, 2)]
    for n in range(1, len(pairs)):
        totnew = reduce(add, reversed(pairs[:n]))
        if totnew == tot:
            print("\nConverge at k=%d"%(2*(n-1)))
            break
        tot = totnew
        print(n*2, tot, end="\t")
    print(tot, "Error", abs(tot.value()/trueValue-1))

    print("(e.ii)")
    tot = FiniteDicimal(num=1)/e55
    print(tot, "Error", abs(tot.value()/trueValue-1))

