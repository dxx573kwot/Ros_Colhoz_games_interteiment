from multiprocessing import Process
import librosa


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


if __name__ == '__main__':
    p = Process(target=musik_render_Sacrifice, args=("Musik/Sacrifice.wav",))
    p1 = Process(target=musik_render_Forever_Mine, args=("Musik/Forever_Mine.wav",))
    p2 = Process(target=musik_render_The_Jounrey_Home, args=("Musik/The_Jounrey_Home.wav",))
    p.start()
    p1.start()
    p2.start()
    p.join()
    p1.join()
    p2.join()
    print(0)