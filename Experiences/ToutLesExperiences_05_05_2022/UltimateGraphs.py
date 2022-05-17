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
                    times.append(time)
                if filename[-5] =="2":
                    times.append(time + 0.5)
                if filename[-5] =="1":
                    times.append(time + 1)
            else: 
                times.append(time)
            readedlist = readlist(file)
        return [list_ppm, times]

def plotGraph( filename : str):
    list_ppm,times= doneesPourGraphs(filename)
    plt.plot(times, list_ppm)
    plt.xlabel("Temps(s)")
    plt.ylabel("CO2 (ppm)")
    titlename = filename.split('/')[0]
    plt.title(titlename) #https://stackoverflow.com/questions/8162021/analyzing-string-input-until-it-reaches-a-certain-letter-on-python
    plt.legend(["Capteur1","Capteur2", "Capteur3"])
    plt.savefig(titlename + '.png')

def plotMultipleGraphs(nb_graph : int, filenames : list[str]):
    for files in filenames:
        if files == "Etalonage/ETA2.TXT":
            list_ppm = []
            times = []
            for filename in ["Etalonage/Echue/Capteur2/ETA1.TXT","Etalonage/Echue/Capteur2/ETA2.TXT","Etalonage/Echue/Capteur2/ETA3.TXT"]:
                file = open(filename, 'r')
                readedlist = readlist(file)
                ppm, c, h = readedlist
                #time = readmilis(file)
                err_ppm = []
                while readedlist != []:
                    time = readmilis(file)
                    ppm, c, h = readedlist
                    list_ppm.append(ppm)
                    if filename[-5] =="1":
                        times.append(time)
                    if filename[-5] =="2":
                        times.append(time + (652595/ 60000))
                    if filename[-5] =="3":
                        times.append(time + ((652584 + 652595 ) / 60000))
                    readedlist = readlist(file)
            plt.legend(["Capteur1","Capteur2", "Capteur3"])
            plt.plot(times, list_ppm)
        else :
            plotGraph(files)

    

def subplotGraph(nb_graph : int, filenames : list[str]):
    for i in range(len(filenames)):
        list_ppm,times= doneesPourGraphs(filenames[i])
        plt.subplot(nb_graph)
        #plt.errorbar(times, list_ppm, yerr = err_vitesse_billes, fmt='.k', elinewidth=1 )
        plt.plot(times, list_ppm)
        plt.legend(str(i))
    plt.xlabel("Temps(s)")
    plt.ylabel("CO2 (ppm)")
    plt.title(filenames[0][0:len(filenames[0]) - 4])
    """
    linear_model=np.polyfit(temps_billes,vitesse_billes,1)
    linear_model_fn=np.poly1d(linear_model)
    x_s=np.arange(0,max(temps_billes)+0.25, 0.25)
    plt.plot(x_s,linear_model_fn(x_s),color="green")
    plt.ylim(intervale)
    """


def main(filenames : list[str]):
    # 1 <= len(filenames) <= 9 (Single argument to subplot must be a three-digit integer) plt.subplot(nb_graph)
    
    for i in range(len(filenames)):
        plotMultipleGraphs(len(filenames)*100 + 10 +i+1, filenames[i])
        plt.legend(["Capteur1","Capteur2","Capteur3"])
        plt.tight_layout()
        #plt.show()
        plt.clf()
    #for i in range(len(filenames)):

filenames = [["Etalonage/ETA1.TXT","Etalonage/ETA2.TXT","Etalonage/ETA3.TXT"], 
             ["FenetreOuverte3PersonnesEnParlant/BETA1.TXT","FenetreOuverte3PersonnesEnParlant/BETA2.TXT","FenetreOuverte3PersonnesEnParlant/BETA3.TXT"],
             ["PorteEtFenetreOuvert3PersonnesEnParlant/OMEGA1.TXT","PorteEtFenetreOuvert3PersonnesEnParlant/OMEGA2.TXT","PorteEtFenetreOuvert3PersonnesEnParlant/OMEGA3.TXT"],
             ["PorteOuverte3PersonnesEnParlant/ALPHA1.TXT","PorteOuverte3PersonnesEnParlant/ALPHA2.TXT","PorteOuverte3PersonnesEnParlant/ALPHA3.TXT"],
             ["PorteOuverte2PersonnesEnParlant/NEWALPHA1.TXT","PorteOuverte2PersonnesEnParlant/NEWALPHA2.TXT","PorteOuverte2PersonnesEnParlant/NEWALPHA3.TXT",]
             ]
main(filenames)
