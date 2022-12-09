from multiprocessing import Process
import librosa


def musik_render(audio_data):
    print("Рендер " + audio_data + " начат")
    bits_in_minute = 60.0
    y, sr = librosa.load(audio_data)
    y_harmonic, y_percussive = librosa.effects.hpss(y)
    tempo, beat_frames = librosa.beat.beat_track(y=y_percussive, sr=sr, units="time", start_bpm=bits_in_minute,
                                                 trim=True)
    print("Рендер " + audio_data + " окончен")
    print()
    return beat_frames


def musik_render_Sacrifice(audio_data):
    global render_audio_Sacrifice
    print("Рендер " + audio_data + " начат")
    bits_in_minute = 60.0
    y, sr = librosa.load(audio_data)
    y_harmonic, y_percussive = librosa.effects.hpss(y)
    tempo, beat_frames = librosa.beat.beat_track(y=y_percussive, sr=sr, units="time", start_bpm=bits_in_minute,
                                                 trim=True)
    print("Рендер " + audio_data + " окончен")
    print()
    render_audio_Sacrifice = beat_frames


def musik_render_Forever_Mine(audio_data):
    global render_audio_Forever_Mine
    print("Рендер " + audio_data + " начат")
    bits_in_minute = 60.0
    y, sr = librosa.load(audio_data)
    y_harmonic, y_percussive = librosa.effects.hpss(y)
    tempo, beat_frames = librosa.beat.beat_track(y=y_percussive, sr=sr, units="time", start_bpm=bits_in_minute,
                                                 trim=True)
    print("Рендер " + audio_data + " окончен")
    print()
    render_audio_Forever_Mine = beat_frames


def musik_render_The_Jounrey_Home(audio_data):
    global render_audio_The_Jounrey_Home
    print("Рендер " + audio_data + " начат")
    bits_in_minute = 60.0
    y, sr = librosa.load(audio_data)
    y_harmonic, y_percussive = librosa.effects.hpss(y)
    tempo, beat_frames = librosa.beat.beat_track(y=y_percussive, sr=sr, units="time", start_bpm=bits_in_minute,
                                                 trim=True)
    print("Рендер " + audio_data + " окончен")
    print()
    render_audio_The_Jounrey_Home = beat_frames


audio_data_main = 'Musik/main.wav'
audio_data_Sacrifice = 'Musik/Sacrifice.wav'
audio_data_Forever_Mine = 'Musik/Forever_Mine.wav'
audio_data_The_Jounrey_Home = 'Musik/The_Jounrey_Home.wav'
p = Process(target=musik_render_Sacrifice, args=(audio_data_Sacrifice,))
p.start()
p.join()
p1 = Process(target=musik_render_Forever_Mine, args=(audio_data_Forever_Mine,))
p1.start()
p1.join()
p2 = Process(target=musik_render_The_Jounrey_Home, args=(audio_data_The_Jounrey_Home,))
p2.start()
p2.join()
