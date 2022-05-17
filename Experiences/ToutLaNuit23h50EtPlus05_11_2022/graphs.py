from matplotlib import pyplot as plt
import matplotlib
import math
from math import sqrt
#import incertitudes as inc
import numpy as np
from scipy.stats import linregress
import sys 
sys.path.insert(1, '/home/erdi/D_Uni/PEI/Ventilation_CO2/Experiences')

def readtuple(file): return tuple(map(float,file.readline().split()))
def readmilis(file): return (int(file.readline().strip())/(1000 * 60)) 
def readlist(file) : return list(map(float,file.readline().split()))

def transformToMinutes(seconds , minutes = 0, hours = 0):
    return (seconds / 60) + minutes + (hours * 60)

def doneesPourGraphs(filename : str)-> list[list]:
    #returns une liste de liste [temps_billes, vitesse_billes, err_vitesse_billes]
    file = open(filename, 'r')
    readedlist = readlist(file)
    ppm, c, h = readedlist
    #time = readmilis(file)
    list_ppm = []
    times = []
    temperatures = []
    err_ppm = []
    while readedlist != []:
        time = readmilis(file)
        ppm, celsius, h = readedlist
        #err_ppm.append()
        temperatures.append(celsius)
        list_ppm.append(ppm)
        if filename[-5] =="3":
            times.append(time)
        if filename[-5] =="2":
            times.append(time + 1)
        if filename[-5] =="1":
            times.append(time + 2)
        
        readedlist = readlist(file)
    return [list_ppm, times, temperatures]

def plotGraph(nb_graph : int, filename : str):
    list_ppm,times, temperatures= doneesPourGraphs(filename)
    #plt.errorbar(times, list_ppm, yerr = 30)
    plt.scatter(times, list_ppm, s = 1)#https://stackoverflow.com/questions/14827650/pyplot-scatter-plot-marker-size
    #plt.scatter(times, temperatures, s = 0.5, color = "black")
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
    plt.title("Tout ferme personnes dans la salle pendant 11 heures")
    #plt.text(0, transformToMinutes(45, 14, 1) "ouverture de la fenetre 1 heure 14 min", fontsize=8)
    #plt.annotate("ouverture de la fenetre 1 heure 14 min", xy = (transformToMinutes(4,14,1),100), xytext = (3,4),arrowprops=dict(facecolor='black', shrink=0.0005))
    plt.show()

filenames = ["ETLNG1.TXT","ETLNG2.TXT","ETLNG3.TXT"]
main(filenames)