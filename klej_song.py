import os
import fala_track
import fala_mua
import numpy as np
from numpy import r_ as c
import scipy.signal
import scipy.io.wavfile
def klej_song(folder):
    x=np.genfromtxt(fname=folder+"song.txt",dtype=str)
    fala=np.array([])
    for i in np.arange(0,len(x)):
        fala01=fala_track.fala_track(x[i],folder)
        fala02=fala_mua.fala_mua(x[i],folder)
        fala01=fala01+fala02
        fala=c[fala,fala01]

    folderek=folder.strip("/")
    scipy.io.wavfile.write(folder+folderek+'.wav',
                           44100,
                           np.int16(fala/
                                    max(np.abs(fala))
                                    *32767))