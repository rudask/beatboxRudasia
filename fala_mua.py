import numpy as np
from numpy import r_ as c
import scipy.signal
import scipy.io.wavfile
def fala_mua(ktory,folder):
    miedzy_nr=2
    miedzy_liter=1.1224620534321632
    miedzy_pol=1.0594630994594263
    cyfry=np.arange(0,10)-4
    litery=np.array(['C','D','E','F','G','A','B'])
    x=np.genfromtxt(fname=folder+"track"+ktory+".txt",dtype=str,comments='?')
    mian=len(x[0,:])
    x=x[:,0]
    cyferki=np.repeat(0,len(x))
    literki=np.repeat("",len(x))
    polowki=np.repeat("",len(x))
    for i in np.arange(0,len(x)):
        if x[i]!="---":
            cyferki[i]=int(x[i][2])
            literki[i]=x[i][0]
            polowki[i]=x[i][1]
    czest=np.repeat(440,len(x))
    czest[np.where (x=="---")]=0;
    cyferki_nowe=cyferki-4
    for i in np.arange(0,len(x)):
        if x[i]!='---':
            if cyferki_nowe[i]<0:
                czest[i]=czest[i]/(miedzy_nr**np.abs(cyferki_nowe[i]))
            if cyferki_nowe[i]>0:
                czest[i]=czest[i]*miedzy_nr**cyferki_nowe[i]
    literki_poz=np.repeat(0,len(x))
    for i in np.arange(0,len(litery)):
        literki_poz[np.where(literki==litery[i])]=i-5
    for i in np.arange(0,len(x)):
        if literki_poz[i]<0:
            czest[i]=czest[i]/(miedzy_liter**np.abs(literki_poz[i]))
        if literki_poz[i]>0:
            czest[i]=czest[i]*miedzy_liter**literki_poz[i]
    czest[np.where(polowki=="#")]=czest[np.where(polowki=="#")]*miedzy_pol
    s = open(folder+'defs.txt', 'r')
    newDict={}
    for line in s:
        listedline = line.strip().split(':')
        if len(listedline) > 1:
            newDict[listedline[0]] = float(listedline[1])
    timebeat=60/newDict['bpm']
    dl=len(x)
    dl_track=dl*timebeat
    dl_track_czest=dl*timebeat*44100
    t = np.linspace(0, dl_track, dl_track_czest)
    f=np.repeat(0,len(t))
    for i in np.arange(0,len(czest)):
        f_temp=np.repeat(czest[i],len(t)/len(czest))
        f[i*len(t)/len(czest):((i+1)*len(t)/len(czest))]=f_temp
    fala=np.sin(2*np.pi*f*t)/mian
    return fala