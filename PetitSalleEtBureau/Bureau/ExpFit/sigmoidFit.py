from matplotlib import pyplot as plt
import numpy as np

def readlist(file) : return list(map(float,file.readline().split()))

def doneesPourGraphs(filename : str)-> list[list]:
    #prends les donnes du fichier donee
    file = open(filename, 'r') #ouverture des fichiers
    readedlist = readlist(file)
    print(readedlist)
    ppm, time= readedlist
    list_ppm = []
    times = []
    i = 0
    while readedlist != []:
        ppm, time = readedlist
        time = time / 1000 #transforms miliseconds to seconds
        if i % 200 == 0:    
            list_ppm.append(ppm)
            times.append(time)
        readedlist = readlist(file)
        i += 1
    return [list_ppm, times]

filenames = ["DONNEES.TXT"]

list_ppm, times= doneesPourGraphs(filenames[0]) #on prend nos donees 

def plot2D(x,y):
    plt.plot(x,y)

def R(n,f,v,Csat, C0):
    return (n*f)/(v-((Csat-C0)/1_000_000))

#def Ct(C0, Csat, r, t):
#    return (C0-Csat)*np.exp(-r*t)+Csat
def Ct(C0, Csat, r, t):
    return (Csat) / (1 + (np.exp(-t)))

#fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
for Csat in range(1750, 10000, 250):
    C0, n, f, v = [550,  3, 0.02, 40]
    #x = np.array(list_ppm)
    #y = np.array(times)
    x = np.linspace(0,1000*60, 2000)#temps en secondes
    y = Ct(C0,Csat, R(n,f,v,Csat,C0), x)
    plot2D(x,y)
plt.ylabel("Ct")
plt.xlabel("time(s)")
plt.show()