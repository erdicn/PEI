from matplotlib import pyplot as plt
from math import sqrt, exp
#import incertitudes as inc
import numpy as np
from scipy.stats import linregress
import sys 
sys.path.insert(1, '/home/erdi/D_Uni/PEI/Ventilation_CO2/Experiences')
from scipy.optimize import curve_fit

def readtuple(file): return tuple(map(float,file.readline().split()))
def readmilis(file): return (int(file.readline().strip())/(1000 * 60)) 
def readlist(file) : return list(map(float,file.readline().split()))

def transformToMinutes(seconds , minutes = 0, hours = 0):
    return (seconds / 60) + minutes + (hours * 60)

def transformToHours(seconds, minutes = 0, hours = 0):
    return (seconds / 3600) + (minutes/60) + (hours)

def milisToHours(milliseconds): return milliseconds /(1000 * 60 * 60)
def milisToMinutes(milliseconds): return milliseconds /(1000 * 60 )

def calculCO2SensorIncertitude(ppm):
    #incertitude +- 30 ppm + 3%
    return 30 + ((3*ppm) / 100)

def equation(C_0, C_ext, r,t):
    return (C_0 - C_ext) * np.exp(-r*t) + C_ext

def memeEquation(C_0, C_sat, r,t):
    return (C_0 - C_sat) * np.exp(-r*t) + C_sat

def findC_sat(C_ext, n,f,r,V):
    return C_ext + ((n*f) / (r*V))

def Cpoint(r,C_sat): #derieve du temps par rapport au temps
    return r*(C_sat - r)

def findr( ppm , n,V ,f = 0.02):
    return (n*f) / (V * (ppm/1_000_000))

V_bureau = 40 #m3
f = 0.02 #m3/h (de CO2)
n = 3 # 3 personnes
C_0 = 750
C_ext = 750
r = 1.5
C_t = [] 
times = np.arange(0, 1_000_000, 1000)
for dt in times:
    C_t.append(equation(C_0, findC_sat(C_ext, n, f, r, V_bureau), r, dt))

plt.scatter(times, C_t)
plt.show()