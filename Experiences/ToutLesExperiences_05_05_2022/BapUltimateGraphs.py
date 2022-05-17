from matplotlib import pyplot as plt
import matplotlib
import math
from math import sqrt
#import incertitudes as inc
import numpy as np

def readtuple(file): return tuple(map(float,file.readline().split()))
def readmilis(file): return (int(file.readline().strip())/(1000 * 60)) 
def readlist(file) : return list(map(float,file.readline().split()))
def readfloat(file): return float(file.readline().strip())
def readstr(file): return file.readline().strip()

def doneesPourGraphs(filename : str)-> list[list]:
    #returns une liste de liste [temps_billes, vitesse_billes, err_vitesse_billes]
    if filename == "Etalonage/ETA3.TXT":
        file = open(filename, 'r')
        ppm = readstr(file)
        list_ppm = []
        times = []
        err_ppm = []
        while ppm != '':
            ppm = float(ppm)
            time = readmilis(file)
            list_ppm.append(ppm)
            #list_ppm.append(ppm+368.59)
            times.append(time)
            ppm = readstr(file)
        return [list_ppm, times]

    else:
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
            if filename[:8] != "Etalonage":
                if filename[-5] =="3":
                    #list_ppm.append(ppm+368.59)
                    times.append(time)
                if filename[-5] =="2":
                    #list_ppm.append(ppm-231.56)
                    times.append(time + 0.5)
                if filename[-5] =="1":
                    #list_ppm.append(ppm+65.80)
                    times.append(time + 1)
            else: 
                times.append(time)
            readedlist = readlist(file)
        return [list_ppm, times]

filenames = [["Etalonage/ETA1.TXT","Etalonage/ETA2.TXT","Etalonage/ETA3.TXT"], 
             ["FenetreOuverte3PersonnesEnParlant/BETA1.TXT","FenetreOuverte3PersonnesEnParlant/BETA2.TXT","FenetreOuverte3PersonnesEnParlant/BETA3.TXT"],
             ["PorteEtFenetreOuvert3PersonnesEnParlant/OMEGA1.TXT","PorteEtFenetreOuvert3PersonnesEnParlant/OMEGA2.TXT","PorteEtFenetreOuvert3PersonnesEnParlant/OMEGA3.TXT"],
             ["PorteOuverte3PersonnesEnParlant/ALPHA1.TXT","PorteOuverte3PersonnesEnParlant/ALPHA2.TXT","PorteOuverte3PersonnesEnParlant/ALPHA3.TXT"],
             ["PorteOuverte2PersonnesEnParlant/NEWALPHA1.TXT","PorteOuverte2PersonnesEnParlant/NEWALPHA2.TXT","PorteOuverte2PersonnesEnParlant/NEWALPHA3.TXT",]
             ]
#main(filenames)

def errorb(l: list[float]):
    eb=[]
    for i in range(0,len(l)):
        eb.append(30+(3/100)*l[i])
    return eb

def graphe_ultime(filenames : list[str]):
    fig, ax = plt.subplots(2,2,sharex=True, constrained_layout=True, figsize = (15,10))
    ax[0,0].set_xlabel("Temps (min)")
    ax[0,1].set_xlabel("Temps (min)")
    ax[1,1].set_xlabel("Temps (min)")
    ax[1,0].set_xlabel("Temps (min)")
    ex1=[]
    ex2=[]
    ex3=[]
    er1=[]
    er2=[]
    er3=[]
    for i in range(1,len(filenames)): #Pas 0 car on ne veut pas l'étalonnage
        ex1=doneesPourGraphs(filenames[i][0])
        ex2=doneesPourGraphs(filenames[i][1])
        ex3=doneesPourGraphs(filenames[i][2])
        #ax[i-1].scatter(x = ex1[1], y = ex1[0],s=1, color='b', label = 'capteur 1')
        #ax[i-1].scatter(x = ex2[1], y= ex2[0],s=1, color='r', label = 'Capteur 2') 
        #ax[i-1].scatter(x = ex3[1], y= ex3[0],s=1, color='g', label = 'Capteur 3')
        if i==1:
            ax[i-1,0].errorbar(ex1[1],ex1[0], yerr=errorb(ex1[0]),elinewidth=0.1,fmt='o',markersize=1, color='b',label='capteur 1')
            ax[i-1,0].errorbar(ex2[1],ex2[0], yerr=errorb(ex2[0]),elinewidth=0.1,fmt='o',markersize=1, color='r',label='capteur 2')
            ax[i-1,0].errorbar(ex3[1],ex3[0], yerr=errorb(ex3[0]),elinewidth=0.1,fmt='o',markersize=1, color='g',label='capteur 3')
        if i==2:
            ax[0,1].errorbar(ex1[1],ex1[0], yerr=errorb(ex1[0]),elinewidth=0.1,fmt='o',markersize=1, color='b')
            ax[0,1].errorbar(ex2[1],ex2[0], yerr=errorb(ex2[0]),elinewidth=0.1,fmt='o',markersize=1, color='r')
            ax[0,1].errorbar(ex3[1],ex3[0], yerr=errorb(ex3[0]),elinewidth=0.1,fmt='o',markersize=1, color='g')
        if i==3:
            ax[1,0].errorbar(ex1[1],ex1[0], yerr=errorb(ex1[0]),elinewidth=0.1,fmt='o',markersize=1, color='b')
            ax[1,0].errorbar(ex2[1],ex2[0], yerr=errorb(ex2[0]),elinewidth=0.1,fmt='o',markersize=1, color='r')
            ax[1,0].errorbar(ex3[1],ex3[0], yerr=errorb(ex3[0]),elinewidth=0.1,fmt='o',markersize=1, color='g')
        if i==4:
            ax[1,1].errorbar(ex1[1],ex1[0], yerr=errorb(ex1[0]),elinewidth=0.1,fmt='o',markersize=1, color='b')
            ax[1,1].errorbar(ex2[1],ex2[0], yerr=errorb(ex2[0]),elinewidth=0.1,fmt='o',markersize=1, color='r')
            ax[1,1].errorbar(ex3[1],ex3[0], yerr=errorb(ex3[0]),elinewidth=0.1,fmt='o',markersize=1, color='g')
    ax[0,0].set_ylabel("CO2 (ppm)")
    ax[0,1].set_ylabel("CO2 (ppm)")
    ax[1,0].set_ylabel("CO2 (ppm)")
    ax[1,1].set_ylabel("CO2 (ppm)")
    ax[0,0].set_title('Fenêtre ouverte et 3 personnes')
    ax[0,1].set_title('Porte et Fenêtre ouvertent et 3 personnes')
    ax[1,0].set_title('Porte ouverte et 3 personnes')
    ax[1,1].set_title('Porte ouverte et 2 personnes')
    handels=[]
    labels=[]
    Handel, Label = ax[0,0].get_legend_handles_labels()
    handels.extend(Handel)
    labels.extend(Label)
    fig.suptitle('Concentration de CO2 en fonction du temps dans une pièce aérée')
    fig.legend(handels,labels, loc = 'upper right')
    plt.savefig("Concentration de CO2 en fonction du temps dans une pièce aérée", dpi = 900)
    plt.show()

graphe_ultime(filenames)
