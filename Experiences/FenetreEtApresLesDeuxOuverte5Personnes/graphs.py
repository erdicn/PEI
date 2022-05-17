from matplotlib import pyplot as plt
import matplotlib
import math
from math import sqrt
#import incertitudes as inc
import numpy as np
#from scipy.stats import linregress

def readtuple(file): return tuple(map(float,file.readline().split()))
def readmilis(file): return (int(file.readline().strip())/(1000 * 60)) 
def readlist(file) : return list(map(float,file.readline().split()))

def transformToMinutes(seconds , minutes = 0, hours = 0):
    return (seconds / 60) + minutes + (hours * 60)

def calculCO2SensorIncertitude(ppm):
    #incertitude +- 30 ppm + 3%
    return 30 + ((3*ppm) / 100)

def doneesPourGraphs(filename : str)-> list[list]:
    #returns une liste de liste [temps_billes, vitesse_billes, err_vitesse_billes]
    file = open(filename, 'r')
    readedlist = readlist(file)
    ppm, c, h = readedlist
    #time = readmilis(file)
    list_ppm = []
    times = []
    err_ppm = []
    while readedlist != []:
        time = readmilis(file)
        ppm, c, h = readedlist
        list_ppm.append(ppm)
        err_ppm.append(calculCO2SensorIncertitude(ppm))
        if filename[-5] =="3":
            times.append(time)
        if filename[-5] =="2":
            times.append(time - transformToMinutes(0, 1))
        if filename[-5] =="1":
            times.append(time - transformToMinutes(54, 1))
        
        readedlist = readlist(file)
    return [list_ppm, times, err_ppm]

def plotGraph(nb_graph : int, filename : str):
    list_ppm, times, err_ppm= doneesPourGraphs(filename)
    plt.errorbar(times, list_ppm, yerr = err_ppm, elinewidth=0.1, markeredgewidth=2, fmt="o", markersize='0.5')#, fmt="o", markersize='0.3', capsize=0.5
    #plt.scatter(times, list_ppm)#https://stackoverflow.com/questions/14827650/pyplot-scatter-plot-marker-size # s = 1 #point size
    #plt.plot(times, list_ppm)
    plt.xlabel("Temps(m)")
    plt.ylabel("CO2 (ppm)")
    """
    plt.subplot(nb_graph)
    #plt.errorbar(times, list_ppm, yerr = err_vitesse_billes, fmt='.k', elinewidth=1 )
    plt.scatter(times, list_ppm)
    plt.xlabel("Temps(s)")
    plt.ylabel("CO2 (ppm)")
    plt.title(filename[0: len(filename) - 4])
    """
    """
    linear_model=np.polyfit(times,list_ppm,1)
    linear_model_fn=np.poly1d(linear_model)
    x_s=np.arange(0,max(times)+0.25, 0.25)
    plt.plot(x_s,linear_model_fn(x_s),color="red",linewidth=0.5)
    """
    #print(linregress(times, list_ppm))
    #plt.ylim(intervale)
    #plt.subplots(sharex=True,constrained_layout=True)

def main(filenames : list[str]):
    # 1 <= len(filenames) <= 9 (Single argument to subplot must be a three-digit integer) plt.subplot(nb_graph)
    for i in range(len(filenames)):
        plotGraph(i+1, filenames[i])
    #plt.axvline(transformToMinutes(4,14,1), color = 'black', linewidth = 1) # vertical ,color='b'
    plt.legend(filenames)
    plt.title("Porte Ouverte a 20 min apres ouverture de la fenetre a 40 min 5 Personnes")
    #plt.text(0, transformToMinutes(45, 14, 1) "ouverture de la fenetre 1 heure 14 min", fontsize=8)
    #plt.annotate("ouverture de la fenetre 1 heure 14 min", xy = (transformToMinutes(4,14,1),100), xytext = (3,4),arrowprops=dict(facecolor='black', shrink=0.0005))
    plt.show()

filenames = ["ULTIQ1.TXT","ULTIQ2.TXT","ULTIQ3.TXT"]
main(filenames) # at 34 sec i started the crono

##################################################################################
#Faire des experiences avec plus de temps que en vois la montee et descente du CO2
##################################################################################