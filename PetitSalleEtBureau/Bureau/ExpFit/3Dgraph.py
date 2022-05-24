"""
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
 
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
        time = time / (1000 ) 
        if i % 1 == 0:    
            list_ppm.append(ppm)
            times.append(time)
        readedlist = readlist(file)
        i += 1
    return [list_ppm, times]

filenames = ["DONNEES.TXT"]
list_ppm,times= doneesPourGraphs(filenames[0])#on prend nos donees 
times = np.array(times)
list_ppm = np.array(list_ppm)
def plot3D(z,x,y):
    #fig = plt.figure()
    
    # syntax for 3-D projection
    #ax = plt.axes(projection ='3d')
    
    # defining all 3 axes
    z = z
    x = x
    y = y
    
    # plotting
    ax.plot3D(x, y, z)
    #plt.show()

def R(n,f,v,Csat, C0):
    return (n*f)/(v-((Csat-C0)/1_000_000))

def Ct(C0, Csat, r, t):
    return (C0-Csat)*np.exp(-r*t)+Csat

def Csat(Ct, C0, r, t):
    return (Ct - (C0*(np.exp(-r*t)))) / (-np.exp(-r*t)-1)

fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
i = 0
r = 1.5
print(len(times))
for t in times:
    C0, n, f, v = [550,  3, 0.02, 40]
    #x = np.array(list_ppm)
    #y = np.array(times)
    x = np.linspace(0,20000, len(times))
    y = Csat(list_ppm[i] / 1_000_000, C0,r, x )
    z = 0
    plot3D(z,x,y)
    #r = R(n,f,v, Csat(list_ppm[i] / 1_000_000, C0,r, x ), C0)
    i += 1
ax.set_xlabel("time(s)")
ax.set_ylabel("ppm")
#ax.set_zlabel("Csat value")
plt.show()
"""
#"""
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
 
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
        time = time / (1000 * 60 ) #transforms miliseconds to minutes
        if i % 200 == 0:    
            list_ppm.append(ppm)
            times.append(time)
        readedlist = readlist(file)
        i += 1
    return [list_ppm, times]

filenames = ["DONNEES.TXT"]
list_ppm,times= doneesPourGraphs(filenames[0])#on prend nos donees 

def plot3D(z,x,y):
    #fig = plt.figure()
    
    # syntax for 3-D projection
    #ax = plt.axes(projection ='3d')
    
    # defining all 3 axes
    z = z
    x = x
    y = y
    
    # plotting
    ax.plot3D(x, y, z)
    #plt.show()

def R(n,f,v,Csat, C0):
    return (n*f)/(v-((Csat-C0)/1_000_000))

def Ct(C0, Csat, r, t):
    return (C0-Csat)*np.exp(-r*t)+Csat

fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
for Csat in range(0, 10000, 250):
    C0, n, f, v = [550,  3, 0.02, 40]
    #x = np.array(list_ppm)
    #y = np.array(times)
    x = np.linspace(0,1000*60, 2000)
    y = Ct(C0,Csat, R(n,f,v,Csat,C0), x)
    z = Csat
    plot3D(z,x,y)
ax.set_xlabel("time(s)")
ax.set_ylabel("ppm")
#ax.set_zlabel("Csat value")
#plt.savefig()
plt.show()
#"""
"""
#ppms = np.array(list_ppm)
#times = np.array(times)
# defining surface and axes
#x = times
#y = list_ppm
x = np.array(list_ppm)
y = np.array(times)
z = x + y
 
fig = plt.figure()
 
# syntax for 3-D plotting
ax = plt.axes(projection ='3d')
 
# syntax for plotting
ax.plot_trisurf(x, y, z, cmap ='viridis', edgecolor ='green')
ax.set_title('Surface plot geeks for geeks')
ax.set_xlabel("ppm")
ax.set_ylabel("time(min)")
ax.set_label("func")
plt.show(block=False)
plt.pause(60)
plt.close()
"""