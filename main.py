import time
import librosa.display
import numpy as np
import pygame
pygame.init()
audio_data = 'Musik/main.wav'
pygame.mixer.music.load(audio_data)
tr, tic, toc = 0, 0, 0
bits_in_minute = 60.0
er = 1
a = 0
i = 0
y, sr = librosa.load(audio_data)
print(type(y), type(sr))
y_harmonic, y_percussive = librosa.effects.hpss(y)
tempo, beat_frames = librosa.beat.beat_track(y=y_percussive, sr=sr, units="time", trim=True)
print('Detected Tempo: ' + str(tempo) + ' beats/min')
beat_times = librosa.frames_to_time(beat_frames, sr=sr)
beat_time_diff = np.ediff1d(beat_times)
beat_nums = np.arange(1, np.size(beat_times))
pygame.mixer.music.play()
toc = 0.1
while True:
    tic = time.perf_counter()
    if i > beat_frames[a]:
        a += 1
        print(1)
    '''print(i)
    print(beat_frames[a])
    print()'''

    i = i + (tic - toc)
    toc = time.perf_counter()
'''for i in beat_frames:
    # print(i, "секунда")
    time.sleep(i - tr - (toc - tic))
    tic = time.perf_counter()
    # основной код начинается
    print("BIT", er)
    tr = i
    er += 1
    print()
    # основной код заканчивается
    toc = time.perf_counter()'''
