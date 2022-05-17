from matplotlib import pyplot as plt
import matplotlib
import math
from math import sqrt
import incertitudes as inc
#import numpy as np

def readtuple(file): return tuple(map(float,file.readline().split()))
def readmilis(file): return (int(file.readline().strip())/(1000)) #in minutes 
def readlist(file): return list(map(float,file.readline().split()))

#calcul de distance en deux dimensions
def calculDistance2D(x0, y0, x1,y1): 
    return sqrt((x0-x1)**2 + (y0-y1)**2) 

def calculVitesse(temps_ecoule, distance_parcourue):
    return distance_parcourue/temps_ecoule

file = open("billes1.txt", 'r')

# gets rid of the first two lines 
file.readline() 
file.readline() 

temps_billes1 = []
xy_billes1 = []
vitesse_billes1 = []
t = readtuple(file)
while t != ():
    temps, x_dis, y_dis = t #x displacement y displacement
    temps_billes1.append(temps)
    xy_billes1.append((x_dis, y_dis))

    if len(temps_billes1) == 1:
        vitesse_billes1.append( calculVitesse(temps_billes1[-1], calculDistance2D(0,0, x_dis, y_dis) ) )
    else:
        x0, y0 = xy_billes1[-2]
        vitesse_billes1.append( calculVitesse(temps_billes1[-1] - temps_billes1[-2], calculDistance2D(x0, y0, x_dis, y_dis) ) )
    
    t = readtuple(file)

file = open("billes2.txt", 'r')

# gets rid of the first two lines 
file.readline() 
file.readline() 

temps_billes2 = []
xy_billes2 = []
vitesse_billes2 = []
t = readtuple(file)
while t != ():
    temps, x_dis, y_dis = t #x displacement y displacement
    temps_billes2.append(temps)
    xy_billes2.append((x_dis, y_dis))

    if len(temps_billes2) == 1:                           #      v  otherwise it divides by 0
        vitesse_billes2.append( calculVitesse(temps_billes2[-1]+0.0000001, calculDistance2D(0,0, x_dis, y_dis) ) )
    else:
        x0, y0 = xy_billes2[-2]
        vitesse_billes2.append( calculVitesse(temps_billes2[-1] - temps_billes2[-2], calculDistance2D(x0, y0, x_dis, y_dis) ) )
    
    t = readtuple(file)

file = open("billes3.txt", 'r')

# gets rid of the first two lines 
file.readline() 
file.readline() 

temps_billes3 = []
xy_billes3 = []
vitesse_billes3 = []
t = readtuple(file)
while t != ():
    temps, x_dis, y_dis = t #x displacement y displacement
    temps_billes3.append(temps)
    xy_billes3.append((x_dis, y_dis))

    if len(temps_billes3) == 1:
        vitesse_billes3.append( calculVitesse(temps_billes3[-1]+0.0000001, calculDistance2D(0,0, x_dis, y_dis) ) )
    else:
        x0, y0 = xy_billes3[-2]
        vitesse_billes3.append( calculVitesse(temps_billes3[-1] - temps_billes3[-2], calculDistance2D(x0, y0, x_dis, y_dis) ) )
    
    t = readtuple(file)

file = open("billes4.txt", 'r')

# gets rid of the first two lines 
file.readline() 
file.readline() 

temps_billes4 = []
xy_billes4 = []
vitesse_billes4 = []
t = readtuple(file)
while t != ():
    temps, x_dis, y_dis = t #x displacement y displacement
    temps_billes4.append(temps)
    xy_billes4.append((x_dis, y_dis))

    if len(temps_billes4) == 1:
        vitesse_billes4.append( calculVitesse(temps_billes4[-1]+0.0000001, calculDistance2D(0,0, x_dis, y_dis) ) )
    else:
        x0, y0 = xy_billes4[-2]
        vitesse_billes4.append( calculVitesse(temps_billes4[-1] - temps_billes4[-2], calculDistance2D(x0, y0, x_dis, y_dis) ) )
    
    t = readtuple(file)

#print(len(vitesse_billes1), len(temps_billes1))
#print(time)
plt.subplot(411)
plt.scatter(temps_billes1, vitesse_billes1)
#plt.errorbar(time, co2, yerr = co2err, fmt='.k', elinewidth=0.1 )
plt.xlabel("Temps(s)")
plt.ylabel("Vitesse (m/s)")
plt.title("billes1")
#plt.ylim(ymin=0, ymax= 1200)
#plt.errorbar();

plt.subplot(412)
plt.scatter(temps_billes2, vitesse_billes2)
#plt.errorbar(time, co2, yerr = co2err, fmt='.k', elinewidth=0.1 )
plt.xlabel("Temps(s)")
plt.ylabel("Vitesse (m/s)")
plt.title("billes2")

plt.subplot(413)
plt.scatter(temps_billes3, vitesse_billes3)
#plt.errorbar(time, co2, yerr = co2err, fmt='.k', elinewidth=0.1 )
plt.xlabel("Temps(s)")
plt.ylabel("Vitesse (m/s)")
plt.title("billes3")

plt.subplot(414)
plt.scatter(temps_billes4, vitesse_billes4)
#plt.errorbar(time, co2, yerr = co2err, fmt='.k', elinewidth=0.1 )
plt.xlabel("Temps(s)")
plt.ylabel("Vitesse (m/s)")
plt.title("billes4")
"""
plt.subplot(312)
plt.scatter(time, co2, s = 5)
#plt.errorbar(time, co2, yerr = incertitude_ppm, fmt='.k' )
plt.xlabel("Temps(s)")
plt.ylabel("CO2 PPM")
#plt.ylim(ymin=0, ymax= 1200)
#plt.errorbar();
"""
"""
linear_model=np.polyfit(temps,uN_U0,1)
linear_model_fn=np.poly1d(linear_model)
x_s=np.arange(80)
plt.plot(x_s,linear_model_fn(x_s),color="green")
"""
plt.show()