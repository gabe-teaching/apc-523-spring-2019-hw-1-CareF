#!/usr/bin/env python
# -*- coding:utf-8 -*-
import numpy as np

ns = 10**np.arange(20)
esequence = (1+1/ns)**ns
error = np.abs(np.diff(esequence)/esequence[1:])
nstop = np.argmax(error < 10**(-12)) 
print("n-stop:", ns[nstop], "value:", esequence[nstop])
print(esequence[:nstop+1])
#  print(error[:nstop+2])
