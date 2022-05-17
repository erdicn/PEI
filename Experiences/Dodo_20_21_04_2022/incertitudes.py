from ast import List
from sympy import diff,symbols
from math import sqrt
import sys

def readfloat(): return list(map(float,sys.stdin.readline().split()))

def moyenne(l: list)->float:
    """ Calcul la moyenne des nombres d'une liste l """  
    return sum(l) / len(l)

def moy_ecarts_moy(l: List)->float:
    """ Calcul de la dispersion par la moyenne des ecarts moyens """
    N = len(l)
    moy = moyenne(l)
    sumxi_moyx = 0
    for i in range(N):
        sumxi_moyx += l[i] - moy
    return (1 / N) * abs(sumxi_moyx)

def ecart_type(l: List)->float:
    N = len(l)
    moy = moyenne(l)
    sumxi_moyx2 = 0
    for i in range(N):
        sumxi_moyx2 += (l[i] - moy)*(l[i] - moy)
    return sqrt((1 / ( N - 1 )) * sumxi_moyx2)

def derive(func : str)->str:
    """Calcul la dérivé d'une fonction avec ses incertitudes - bloqué à 3 variables max !"""
    inc_func = 0
    a =int(input("Give the number of variables:"))
    ecart_tf= [float(a) for a in input("Enter the incertitudes for all of you variables: ").split()]
    if a==1:
        x=symbols('x')
        vars=[x]
    elif a==2:
        x,y=symbols('x,y')
        vars = [x,y]
    else:
        x,y,z = symbols('x,y,z')
        vars = [x,y,z]
    for i in range(len(vars)):
        inc_func += diff(func, vars[i])*ecart_tf[i]
    return inc_func

##########################################
#print(derive(input("The function to derivate: ")))
##########################################

def derived_func_value():
    ##########################################
    x,y,z = (5, 10 ,15)
    return -0.15*y/z**2 + 1.0 + 3/z #put the inc_func here but paste it from terminal
    ##########################################

#print(derived_func_value())
dfv = [derived_func_value() for i in range(3)]
#print(dfv)
