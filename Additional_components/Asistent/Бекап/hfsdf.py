import datetime
import torch
import queue
import vosk
import sys
import sounddevice as sd
import time
import config
import random
import subprocess


def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))


def get_time():
    bnm = datetime.datetime.now()
    ghj = config.hour[bnm.strftime("%H")]
    jhg = config.minute[bnm.strftime("%M")]
    return f" {ghj}:{jhg}"


model = vosk.Model("model")
samplerate = 16000
device = 1
if config.fast_with_gpu:
    device2 = torch.device('gpu')
else:
    device2 = torch.device('cpu')
text = config.privetstvie
model2, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
                           model='silero_tts',
                           language=config.language,
                           speaker=config.model_id)

model2.to(device2)
q = queue.Queue()

audio = model2.apply_tts(text=config.privetstvie,
                         speaker=config.speaker,
                         sample_rate=config.sample_rate,
                         put_accent=config.put_accent,
                         put_yo=config.put_yo)

sd.play(audio, config.sample_rate)
time.sleep(len(audio) / config.sample_rate + 1)
sd.stop()


with sd.RawInputStream(samplerate=samplerate, blocksize=8000, device=device, dtype="int16", channels=1,
                       callback=callback):

    rec = vosk.KaldiRecognizer(model, samplerate)
    while True:
        data = q.get()
        if rec.AcceptWaveform(data):

            print("Слушаю")

            asd = rec.Result()
            dsa = ""
            for i in asd:
                dsa += i
            asd = " ".join(dsa.split()[3:-1])

            print(asd)

            if "время" in asd:

                print("Обрабатываю")

                text = get_time()

                print("Конец Обработки")
            elif "открой" in asd:

                for i in config.progi:
                    if i in asd:
                        subprocess.call(config.progi[i])
                    break

            elif config.name in asd:

                print("Обрабатываю")

                text = random.choice(config.otclik)

                print("Конец Обработки")

            else:
                text = ""
            if text != "":

                print("Озвучиваю")

                audio = model2.apply_tts(text=text,
                                         speaker=config.speaker,
                                         sample_rate=config.sample_rate,
                                         put_accent=config.put_accent,
                                         put_yo=config.put_yo)

                print("Произношу")

                sd.play(audio, config.sample_rate)
                time.sleep(len(audio) / config.sample_rate + 1)
                sd.stop()

            text = ""
