from matplotlib import pyplot as plt
#import numpy as np

def readlist(file) : return list(map(float,file.readline().split()))

def transformToMinutes(seconds , minutes = 0, hours = 0):
    return (seconds / 60) + minutes + (hours * 60)

def transformToHours(seconds, minutes = 0, hours = 0):
    return (seconds / 3600) + (minutes/60) + (hours)

def milisToHours(milliseconds): return milliseconds /(1000 * 60 * 60)
def milisToMinutes(milliseconds): return milliseconds /(1000 * 60 )

def calculCO2SensorIncertitude(ppm): 
    # calculates the error of sensors given by the manufacturer 
    #incertitude +- 30 ppm + 3%
    return 30 + ((3*ppm) / 100)

def doneesPourGraphs(filename : str)-> list[list]:
    file = open(filename, 'r') #opens file
    readedlist = readlist(file) # reades the line 
    ppm, c, h, time= readedlist # puts the readed line to values 
    #initialise the lists 
    list_ppm = []
    times = []
    temperatures = []
    err_ppm = []
    #entter in the transformToMinutes each Arduino start time
    startC1 = transformToMinutes(0)
    startC2 = transformToMinutes(40)
    startC3 = transformToMinutes(42,1)
    while readedlist != []: # until we finish the file 
        ppm, celsius, h, time = readedlist 
        time = milisToMinutes(time) 
        temperatures.append(celsius) 
        list_ppm.append(ppm)
        err_ppm.append(calculCO2SensorIncertitude(ppm))
        #Adds the time of each sensorc because we start them at intervals
        if filename[-5] =="3":
            times.append(time + startC3)
        if filename[-5] =="2":
            times.append(time + startC2)
        if filename[-5] =="1":
            times.append(time + startC1)
        readedlist = readlist(file)
    return [list_ppm, times, temperatures, err_ppm]

def plotGraph(nb_graph : int, filename : str,list_ppm,times, temperatures, err_ppm):
    plt.errorbar(times, list_ppm, yerr = err_ppm, elinewidth=0.1, markeredgewidth=2, fmt="o", markersize='0.5')
    plt.xlabel("Temps(m)")
    plt.ylabel("CO2 (ppm)")

def main(filenames : list[str]):
    # 1 <= len(filenames) <= 9 (Single argument to subplot must be a three-digit integer) plt.subplot(nb_graph)
    systematicErreurDuCapteur3 = 426.36
    
    #if we do a calibration we change the systematic error of the sensor nb_3 
    """
    moyennes = []
    for i in range(len(filenames)):
        list_ppm,times, temperatures, err_ppm = doneesPourGraphs(filenames[i])
        moyennes.append((sum(list_ppm)/len(list_ppm)))
    moyenneDe1et2 = (moyennes[0] + moyennes[1]) / 2
    systematicErreurDuCapteur3 = moyennes[2] - moyenneDe1et2
    print(systematicErreurDuCapteur3)
    """
    
    for i in range(len(filenames)):
        list_ppm,times, temperatures, err_ppm = doneesPourGraphs(filenames[i])
        if i == 2: # if we are at the saved file with the sensor number 3
            for j in range(len(list_ppm)): #we correct the systematic error
                list_ppm[j] = list_ppm[j] - systematicErreurDuCapteur3 #sistematicErreurDuCapteur3
            plotGraph(i+1, filenames[i],list_ppm,times, temperatures, err_ppm)
        else:    
            plotGraph(i+1, filenames[i],list_ppm,times, temperatures, err_ppm)

    sensor_legend = ["Capteur 1","Capteur 2","Capteur 3"]    
    plt.legend(sensor_legend)
    plt.title("Petit Salle Porte ferme et ouverture apres un certain temps Avec purificateur")
    plt.savefig("Petit salle avec purficateur",format="pdf", dpi = 900) #Saves the plot 
    plt.show()

filenames = ["CLOSED1.TXT","CLOSED2.TXT","CLOSED3.TXT"] #enter the files with the sensor values
main(filenames)