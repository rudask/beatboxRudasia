import numpy as np
from numpy import r_ as c
import scipy.signal
import scipy.io.wavfile
def fala_track(ktory,folder):
    x=np.genfromtxt(fname=folder+"track"+ktory+".txt",dtype=str,comments='?')
    s = open(folder+'defs.txt', 'r')
    newDict={}
    for line in s:
        listedline = line.strip().split(':')
        if len(listedline) > 1:
            newDict[listedline[0]] = float(listedline[1])
    timebeat=60/newDict['bpm']
    dl=len(x[:,1])
    dl_track=dl*timebeat
    dl_track_czest=dl*timebeat*44100
    dlugosc_track=np.arange(0,dl_track_czest)
    fala=np.repeat(0.0,len(dlugosc_track))
    for j in np.arange(1,len(x[1,:])):

        fs,y = scipy.io.wavfile.read(folder+'sample0'+str(j+1)+'.wav')
       
        y = np.mean(y,axis=1)
        y /= 32767

        dlugosc=np.arange(0,dl_track+timebeat,timebeat)

        ktore=np.array([])
        for i in np.arange(0,len(x[:,1])):
            if x[i,j]=='0'+str(j+1):
                ktore=c[ktore,i]

        wst=dlugosc[ktore.tolist()]
        wst=wst*44100
        dlugosc_track=np.arange(0,dl_track_czest)
        fala01=np.repeat(0.0,len(dlugosc_track))
        for i in np.arange(0,len(wst)):
            if (dl_track_czest-wst[i])>=len(y):
                fala01[wst[i]:(wst[i]+len(y))]+=y
            else:
                y_uc=y[0:(dl_track_czest-wst[i])]
                fala01[wst[i]:(wst[i]+len(y_uc))]+=y_uc

        fala=fala+fala01/len(x[1,:])
    return fala;