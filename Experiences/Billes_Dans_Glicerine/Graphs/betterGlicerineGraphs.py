from matplotlib import pyplot as plt
import matplotlib
import math
from math import sqrt
import incertitudes as inc
import numpy as np

def readtuple(file): return tuple(map(float,file.readline().split()))
def readmilis(file): return (int(file.readline().strip())/(1000)) #in minutes 
def readlist(file) : return list(map(float,file.readline().split()))

#calcul de distance en deux dimensions
def calculDistance2D(x0, y0, x1,y1): 
    return sqrt((x0-x1)**2 + (y0-y1)**2) 

def incertitudeCalculDistance(x0,y0,x1,y1):
    return 5.0e-5*(-x0 + x1)/sqrt((x0 - x1)**2 + (y0 - y1)**2) + 5.0e-5*(x0 - x1)/sqrt((x0 - x1)**2 + (y0 - y1)**2) + 5.0e-5*(-y0 + y1)/sqrt((x0 - x1)**2 + (y0 - y1)**2) + 5.0e-5*(y0 - y1)/sqrt((x0 - x1)**2 + (y0 - y1)**2)

def calculVitesse(temps_ecoule, distance_parcourue):
    return distance_parcourue/temps_ecoule

def incertitudeCalculVitesse( temps_ecoule, x0,y0,x1,y1):
    return calculVitesse(temps_ecoule, calculDistance2D(x0,y0,x1,y1)) * ( (incertitudeCalculDistance(x0,y0,x1,y1) / calculDistance2D(x0,y0,x1,y1)) + ( (1/60) / temps_ecoule) )

def doneesPourGraphs(filename : str)-> list[list]:
    #returns une liste de liste [temps_billes, vitesse_billes, err_vitesse_billes]
    file = open(filename, 'r')
    # gets rid of the first two lines 
    file.readline() 
    file.readline() 
    err_vitesse_billes = []
    temps_billes = []
    xy_billes = []
    vitesse_billes = []
    t = readtuple(file)
    while t != ():
        temps, x_dis, y_dis = t #x displacement y displacement
        temps_billes.append(temps)
        xy_billes.append((x_dis, y_dis))
        x1,y1 = xy_billes[-1]
        if len(temps_billes) == 1:
            x0,y0 = [0,0]
            temps_ecoule = temps_billes[-1] + 0.000000001 #so we dont divise by 0
            vitesse_billes.append(0)
        else:
            x0, y0 = xy_billes[-2]
            temps_ecoule = temps_billes[-1] - temps_billes[-2]
            vitesse_billes.append( calculVitesse(temps_ecoule, calculDistance2D(x0, y0, x1, y1) ) )

        err_vitesse_billes.append(incertitudeCalculVitesse(temps_ecoule, x0,y0,x1,y1))
        t = readtuple(file)
    return [temps_billes, vitesse_billes,err_vitesse_billes]

def plotGraph(nb_graph : int, filename : str, intervale):
    temps_billes, vitesse_billes, err_vitesse_billes = doneesPourGraphs(filename)

    plt.subplot(nb_graph)
    plt.errorbar(temps_billes, vitesse_billes, yerr = err_vitesse_billes, fmt='.k', elinewidth=1 )
    plt.xlabel("Temps(s)")
    plt.ylabel("Vitesse (m/s)")
    plt.title(filename[0: len(filename) - 4])
    linear_model=np.polyfit(temps_billes,vitesse_billes,1)
    linear_model_fn=np.poly1d(linear_model)
    x_s=np.arange(0,max(temps_billes)+0.25, 0.25)
    plt.plot(x_s,linear_model_fn(x_s),color="green")
    plt.ylim(intervale)
    print(filename, len(vitesse_billes))

def main(filenames : list[str] , intervales : list):
    # 1 <= len(filenames) <= 9 (Single argument to subplot must be a three-digit integer) plt.subplot(nb_graph)
    for i in range(len(filenames)):
        plotGraph((len(filenames)*100)+11+i, filenames[i] , intervales[i])
    plt.show()

filenames = ["billes1.txt","billes2.txt","billes3.txt","billes4.txt"]
intervales = [[0,0.1], [0, 0.75], [0, 0.5], [0,2]]
main(filenames,intervales)