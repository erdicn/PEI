from matplotlib import pyplot as plt
import numpy as np

def readlist(file) : return list(map(float,file.readline().split()))

def doneesPourGraphs(filename : str)-> list[list]:
    #prends les donnes du fichier donee
    file = open(filename, 'r') #ouverture des fichiers
    readedlist = readlist(file)
    ppm, time= readedlist
    list_ppm = []
    times = []
    i = 0
    while readedlist != []:
        ppm, time = readedlist
        time = time / 1000 #transforms miliseconds to seconds
        if i % 200 == 0:    
            list_ppm.append(ppm - 566)# to put it at zero
            times.append(time)
        readedlist = readlist(file)
        i += 1
    return [list_ppm, times]

filenames = ["DONNEES.TXT"]
C0 = 566.3
list_ppm,times= doneesPourGraphs(filenames[0])#on prend nos donees 
times = np.array(times)
ppms = np.array(list_ppm)

#print(np.polynomial.polynomial.Polynomial.fit(times, np.log(ppms), 1))
fit = np.polyfit(times, np.log(ppms),1)
print(fit)
#y = np.exp(0.000279273403 + 5.20171927 * times) #ca fait 1 + 
y = 1 + np.exp(5.20171927 * times)

# plot the function
#plt.plot(times,y, 'r')
#plt.scatter(times,ppms)
plt.scatter(ppms,times)
# show the plot
plt.ylim(0,10000)
plt.legend(["function", "times ppms", "ppms times"])
plt.savefig("ExponentialFig", dpi = 300)
plt.show(block=False)
plt.pause(5)
plt.close()