import time

import librosa
import matplotlib
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import IPython.display as ipd
import pygame
pygame.init()
audio_data = 'file.wav'
pygame.mixer.music.load(audio_data)
tr = 0
bits_in_minute = 60.0
er = 1
y, sr = librosa.load(audio_data)
print(type(y), type(sr))
y_harmonic, y_percussive = librosa.effects.hpss(y)
tempo, beat_frames = librosa.beat.beat_track(y=y_percussive, sr=sr, units="time", start_bpm=bits_in_minute, trim=True)
print('Detected Tempo: ' + str(tempo) + ' beats/min')
beat_times = librosa.frames_to_time(beat_frames, sr=sr)
beat_time_diff = np.ediff1d(beat_times)
beat_nums = np.arange(1, np.size(beat_times))
pygame.mixer.music.play()
for i in beat_frames:
    # print(i, "секунда")
    time.sleep(i - tr)
    print("BIT", er)
    tr = i
    er += 1
    print()