from matplotlib import pyplot as plt
import matplotlib
import math
from math import sqrt
#import incertitudes as inc
import numpy as np
from scipy.stats import linregress
import sys 
sys.path.insert(1, '/home/erdi/D_Uni/PEI/Ventilation_CO2/Experiences')
from pylab import *
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

def doneesPourGraphs(filename : str)-> list[list]:
    #returns une liste de liste [temps_billes, vitesse_billes, err_vitesse_billes]
    file = open(filename, 'r')
    readedlist = readlist(file)
    ppm, c, h, time= readedlist
    list_ppm = []
    times = []
    temperatures = []
    err_ppm = []
    startC1 = transformToMinutes(0)
    startC2 = transformToMinutes(57)
    startC3 = transformToMinutes(1,2)
    while readedlist != []:
        ppm, celsius, h, time = readedlist
        time = milisToMinutes(time)
        #err_ppm.append()
        temperatures.append(celsius)
        list_ppm.append(ppm)
        err_ppm.append(calculCO2SensorIncertitude(ppm))
        if filename[-5] =="3":
            times.append(time + startC3)
        if filename[-5] =="2":
            times.append(time + startC2)
        if filename[-5] =="1":
            times.append(time + startC1)
        readedlist = readlist(file)
    #print(filename, "moyenne : ", (sum(list_ppm)/len(list_ppm)))
    return [list_ppm, times, temperatures, err_ppm]

def plotGraph(nb_graph : int, filename : str,list_ppm,times, temperatures, err_ppm):
    #list_ppm,times, temperatures, err_ppm, moyenne= doneesPourGraphs(filename)
    plt.errorbar(times, list_ppm, yerr = err_ppm, elinewidth=0.1, markeredgewidth=2, fmt="o", markersize='0.5')
    #plt.errorbar(times, list_ppm, yerr = 30)
    #plt.scatter(times, list_ppm, s = 1)#https://stackoverflow.com/questions/14827650/pyplot-scatter-plot-marker-size
    #plt.scatter(times, temperatures, s = 0.5, color = "black")
    #plt.plot(times, list_ppm)
    plt.xlabel("Temps(m)")
    plt.ylabel("CO2 (ppm)")
   
    if nb_graph == 0:
        linear_model=np.polyfit(times,list_ppm,1)
        linear_model_fn=np.poly(linear_model)
        x_s=np.arange(0,max(12*60)+0.25, 0.25)
        plt.plot(x_s,linear_model(x_s),color="red",linewidth=10)
        print(linregress(times, list_ppm))

    #plt.ylim(intervale)
    #plt.subplots(sharex=True,constrained_layout=True)
    
def main(filenames : list[str]):
    # 1 <= len(filenames) <= 9 (Single argument to subplot must be a three-digit integer) plt.subplot(nb_graph)
    moyennes = []
    for i in range(len(filenames)):
        list_ppm,times, temperatures, err_ppm = doneesPourGraphs(filenames[i])
        moyennes.append((sum(list_ppm)/len(list_ppm)))
    moyenneDe1et2 = (moyennes[0] + moyennes[1]) / 2
    sistematicErreurDuCapteur3 = moyennes[2] - moyenneDe1et2
    print("Systematic erreur du capteur 3 : ", sistematicErreurDuCapteur3)

    for i in range(len(filenames)):
        list_ppm,times, temperatures, err_ppm = doneesPourGraphs(filenames[i])
        if i == 10: #cest le capteur 3 

            for j in range(len(list_ppm)):
                list_ppm[j] = list_ppm[j] - 426.36 #sistematicErreurDuCapteur3
            plotGraph(i+1, filenames[i],list_ppm,times, temperatures, err_ppm)
            #print(filenames)
        else:    
            plotGraph(i+1, filenames[i],list_ppm,times, temperatures, err_ppm)
    #plt.axvline(transformToMinutes(4,14,1), color = 'black', linewidth = 1) # vertical ,color='b'
    plt.legend(["Capteur 1", "Capteur 2", "Capteur 3"])
    plt.title("Petit Salle Porte ferme et ouverture apres un certain temps")
    plt.savefig("300dpiBureau3heuresPorteOuvete", dpi = 300)
    plt.show()
    
filenames = ["PGRACH1.TXT","PGRACH2.TXT","PGRACH3.TXT"]
main(filenames)


list_ppm,times, temperatures, err_ppm = doneesPourGraphs(filenames[0])
x_data = np.array(times)
y_data = np.array(list_ppm)
print(times)

log_x_data = np.log(x_data) #np.log(x_data)
log_y_data = np.log(y_data)

curve_fit = np.polyfit(x_data, log_y_data, 1)
print(curve_fit)
y = np.exp(1.10157432e-03) * np.exp(7.13657761e+00*x_data)
#y = 4.84 * log_x_data - 10.79
print(y)
plt.plot(x_data, y_data)
  
# best fit in orange
plt.plot(x_data, y)
plt.show()
curve_fit = np.polyfit(x_data, y_data, 1)
print(curve_fit)
y = np.exp(2.74186352) * np.exp(1272.99890017*x_data)
#y = 4.84 * log_x_data - 10.79
print(y)
plt.plot(x_data, y_data)
  
# best fit in orange
plt.plot(x_data, y)
plt.show()
"""
plt.plot(log_x_data, y_data, "o")
plt.plot(log_x_data, y)
plt.show()
"""