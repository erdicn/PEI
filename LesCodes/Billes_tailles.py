from math import pi
from sympy import diff,symbols
from math import sqrt
import plotly.graph_objects as go
import plotly.express as px
import sys

def readfloat(): return list(map(float,sys.stdin.readline().split()))

def moyenne(l: list)->float:
    """ Calcul la moyenne des nombres d'une liste l """  
    return sum(l) / len(l)

def moy_ecarts_moy(l: list)->float:
    """ Calcul de la dispersion par la moyenne des ecarts moyens """
    N = len(l)
    moy = moyenne(l)
    sumxi_moyx = 0
    for i in range(N):
        sumxi_moyx += l[i] - moy
    return (1 / N) * abs(sumxi_moyx)

def ecart_type(l: list)->float:
    N = len(l)
    moy = moyenne(l)
    sumxi_moyx2 = 0
    for i in range(N):
        sumxi_moyx2 += (l[i] - moy)*(l[i] - moy)
    return sqrt((1 / ( N - 1 )) * sumxi_moyx2)

def derive(func : str)->str:
    """Calcul la dérivé d'une fonction avec ses incertitudes - bloqué à 3 variables max !"""
    d, m = symbols("d, m")
    vars = [d, m]
    incer = [0.1 for _ in range(len(vars))]
    for i in range(len(vars)):
        inc_func += diff(func, vars[i])*incer[i]
    return inc_func

#S G M P
tout = [(16.27, 5.66), (7.70, 0.35), (4.96, 0.165), (3.97, 0.084)] 
masse_voluminiques = [ (m / ((4/3) *  pi * (d*d*d)/8))*10**6 for d,m in tout]#divided by 8 because it is the diameter and me need the rayon
print(derive("(m / ((4/3) *  pi * (d*d*d)/8))*10**6"))
print(masse_voluminiques)