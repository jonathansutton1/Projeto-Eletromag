import numpy as np
from math import pi
from cmath import *
import matplotlib.pyplot as plt
from numpy import linalg

w = 120*pi
R1 = 1
R2 = 2
L1=3.148*(10**(-6))
L2=0.283
RC, UF = 1,1
XL1= 1j*w*L1
XL2= 1j*w*L2
k=0.96
XM = sqrt(XL1*XL2)*k

def CalcularTransformador(Uf, Rc):
    Z=np.array([[R1+XL1, -XM],[-XM, XL2+R2+Rc]])
    V=np.array([Uf,0])
    i=np.dot(linalg.inv(Z),V)
    return i[0], i[1]