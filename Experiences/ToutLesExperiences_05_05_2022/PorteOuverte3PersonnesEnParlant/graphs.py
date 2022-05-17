from matplotlib import pyplot as plt
import matplotlib
import math
from math import sqrt
#import incertitudes as inc
import numpy as np

def readtuple(file): return tuple(map(float,file.readline().split()))
def readmilis(file): return (int(file.readline().strip())/(1000 * 60)) 
def readlist(file) : return list(map(float,file.readline().split()))

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
        if filename[-5] =="3":
            times.append(time)
        if filename[-5] =="2":
            times.append(time + 1.5)
        if filename[-5] =="1":
            times.append(time + 3)
        
        readedlist = readlist(file)
    return [list_ppm, times]

def plotGraph(nb_graph : int, filename : str):
    list_ppm,times= doneesPourGraphs(filename)
    #plt.errorbar(times, list_ppm, yerr = 30)
    plt.plot(times, list_ppm)
    """
    plt.subplot(nb_graph)
    #plt.errorbar(times, list_ppm, yerr = err_vitesse_billes, fmt='.k', elinewidth=1 )
    plt.scatter(times, list_ppm)
    plt.xlabel("Temps(s)")
    plt.ylabel("CO2 (ppm)")
    plt.title(filename[0: len(filename) - 4])
    """
    """
    linear_model=np.polyfit(temps_billes,vitesse_billes,1)
    linear_model_fn=np.poly1d(linear_model)
    x_s=np.arange(0,max(temps_billes)+0.25, 0.25)
    plt.plot(x_s,linear_model_fn(x_s),color="green")
    plt.ylim(intervale)
    """
    #plt.subplots(sharex=True,constrained_layout=True)

def main(filenames : list[str]):
    # 1 <= len(filenames) <= 9 (Single argument to subplot must be a three-digit integer) plt.subplot(nb_graph)
    for i in range(len(filenames)):
        plotGraph(i+1, filenames[i])
    plt.legend(filenames)
    plt.title("Porte ouverte 3 personnes entre capteur 2 et 3")
    plt.show()

filenames = ["ALPHA1.TXT","ALPHA2.TXT","ALPHA3.TXT"]
main(filenames)