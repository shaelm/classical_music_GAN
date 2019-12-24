
##preprocessing step of shortening midi files to 15 seconds, some of them were very long and we want them all standard for the GAN
## this way the gan should be generating images that corrospond to 15 seconds clip always.
from scipy import signal
import pretty_midi
import matplotlib.pyplot as plt
import glob
import librosa
import os
from librosa import display
import pypianoroll as pypr


rootdir = ''
fs=5e3 # just default sampling freq ro 3khz for now?
rootdir="C:/Users/shael/PycharmProjects/classical_music_GAN/maestro-v2.0.0-midi"
txt = glob.glob('lmd_full/*.mid') # get all the files in the directory that are midi
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        print(file)
        if file.endswith(".midi"):
            try:
                pm=pretty_midi.PrettyMIDI(os.path.join(subdir,file))
                length=pm.get_end_time()
                print(length)
                pm.adjust_times([0,15],[0,15])# we want to crop to first 15 seconds of midi song
                pm.write("shortenedMIDI/"+str(file))
            except:
                print("Couldnt read file")


