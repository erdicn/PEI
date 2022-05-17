from matplotlib import pyplot as plt
import math
import matplotlib
import incertitudes as inc
#import numpy as np

def readtuple(file): return tuple(map(float,file.readline().split()))
def readmilis(file): return (int(file.readline().strip())/(1000)) #in minutes 
def readlist(file): return list(map(float,file.readline().split()))


file = open("MESURES7.TXT", 'r')
#print(readtuple(file))
time = []
co2  = []

filtre = False

for i in range(0, 502):

    #liste_mesures = readlist(file)
    #print(liste_mesures)
    ppm, humidity , temperature = readtuple(file)
    mili = readmilis(file)

    if not filtre:
        #print(readtuple(file))
        co2.append(ppm)
        time.append(mili)
    if filtre:
        if ppm > 430:#pour filtrer les errrurs
            i += 2
        else:
            co2.append(ppm)
            time.append(mili)
    
incertitude_ppm = inc.ecart_type(co2)
print(incertitude_ppm)
#print(time)
plt.subplot(311)
#plt.scatter(time, co2)

plt.errorbar(time, co2, yerr = incertitude_ppm, fmt='.k', elinewidth=0.1 )
plt.xlabel("Temps(s)")
plt.ylabel("CO2 PPM")

#plt.errorbar();

plt.subplot(312)
plt.scatter(time, co2, s = 5)
#plt.errorbar(time, co2, yerr = incertitude_ppm, fmt='.k' )
plt.xlabel("Temps(s)")
plt.ylabel("CO2 PPM")

#plt.errorbar();

"""
linear_model=np.polyfit(temps,uN_U0,1)
linear_model_fn=np.poly1d(linear_model)
x_s=np.arange(80)
plt.plot(x_s,linear_model_fn(x_s),color="green")
"""
plt.show()