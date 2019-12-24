import pretty_midi
import matplotlib.pyplot as plt
import glob
import librosa
import os
from librosa import display



rootdir = ''
fs=5e3 # just default sampling freq ro 3khz for now?
rootdir="C:/Users/shael/PycharmProjects/classical_music_GAN/shortenedMIDI"
txt = glob.glob('lmd_full/*.mid') # get all the files in the directory that are midi
# Note the blurry section between 1.5s and 2.3s - that's the pitch bending up!
for dir, dirs, files in os.walk(rootdir):
    for file in files:
            try:
                pm=pretty_midi.PrettyMIDI(os.path.join(dir,file))
                print(pm.get_end_time())
                plt.figure(figsize=(8, 4))
                start_pitch=50
                end_pitch=100
                fs=3000
                pr=pm.get_piano_roll(fs)[start_pitch:end_pitch]
                librosa.display.specshow(pr,
                                         hop_length=1, sr=fs, x_axis='time', y_axis='cqt_note',
                                         fmin=pretty_midi.note_number_to_hz(start_pitch))
                plt.show()
            except:
                print("Couldnt read file")
