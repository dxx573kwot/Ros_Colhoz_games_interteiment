import datetime
import torch
import queue
import vosk
import sys
import sounddevice as sd
import time
import random
import subprocess
import sqlite3
import config
import pygame
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import numpy
import setuptools

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
STOPPED_PLAYING = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(STOPPED_PLAYING)


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(730, 300)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 20, 111, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 91, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 60, 55, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(600, 10, 650, 16))
        self.label_4.setObjectName("label_4")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(90, 20, 180, 16))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(90, 40, 180, 16))
        self.textEdit_2.setObjectName("textEdit_2")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(90, 60, 180, 16))
        self.comboBox.setObjectName("textEdit_3")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(690, 10, 700, 20))
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(10, 100, 131, 16))
        self.label_5.setObjectName("label_5")
        self.textEdit_5 = QtWidgets.QTextEdit(Form)
        self.textEdit_5.setGeometry(QtCore.QRect(20, 140, 91, 16))
        self.textEdit_5.setObjectName("textEdit_5")
        self.textEdit_6 = QtWidgets.QTextEdit(Form)
        self.textEdit_6.setGeometry(QtCore.QRect(130, 140, 231, 16))
        self.textEdit_6.setObjectName("textEdit_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(30, 120, 71, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(140, 120, 55, 16))
        self.label_8.setObjectName("label_8")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(380, 130, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(20, 180, 131, 16))
        self.label_6.setObjectName("label_6")
        self.textEdit_7 = QtWidgets.QTextEdit(Form)
        self.textEdit_7.setGeometry(QtCore.QRect(20, 220, 91, 16))
        self.textEdit_7.setObjectName("textEdit_7")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(30, 200, 71, 16))
        self.label_9.setObjectName("label_9")
        self.textEdit_8 = QtWidgets.QTextEdit(Form)
        self.textEdit_8.setGeometry(QtCore.QRect(130, 220, 91, 16))
        self.textEdit_8.setObjectName("textEdit_8")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(130, 200, 81, 20))
        self.label_10.setObjectName("label_10")
        self.textEdit_9 = QtWidgets.QTextEdit(Form)
        self.textEdit_9.setGeometry(QtCore.QRect(240, 220, 91, 16))
        self.textEdit_9.setObjectName("textEdit_9")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(250, 200, 71, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(370, 200, 55, 16))
        self.label_12.setObjectName("label_12")
        self.textEdit_10 = QtWidgets.QTextEdit(Form)
        self.textEdit_10.setGeometry(QtCore.QRect(360, 220, 231, 16))
        self.textEdit_10.setObjectName("textEdit_10")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(610, 220, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 250, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Приветствие"))
        self.label_2.setText(_translate("Form", "Имя"))
        self.label_3.setText(_translate("Form", "Голос"))
        self.label_4.setText(_translate("Form", "Режим отладки"))
        self.label_5.setText(_translate("Form", "Добавить программу"))
        self.label_7.setText(_translate("Form", "Код. слово"))
        self.label_8.setText(_translate("Form", "Адрес"))
        self.pushButton.setText(_translate("Form", "Добавить"))
        self.label_6.setText(_translate("Form", "Добавить музыку"))
        self.label_9.setText(_translate("Form", "Жанр"))
        self.label_10.setText(_translate("Form", "Исполнитель"))
        self.label_11.setText(_translate("Form", "Название"))
        self.label_12.setText(_translate("Form", "Адрес"))
        self.pushButton_2.setText(_translate("Form", "Добавить"))
        self.pushButton_3.setText(_translate("Form", "Сохранить"))


class MyWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        # Вызываем метод для загрузки интерфейса из класса Ui_MainWindow,
        # остальное без изменений
        self.setupUi(self)
        self.pushButton.clicked.connect(lambda: self.plus_proga())
        self.pushButton_2.clicked.connect(lambda: self.plus_musik())
        self.pushButton_3.clicked.connect(self.set_seting)
        self.comboBox.addItem("aidar")
        self.comboBox.addItem("baya")
        self.comboBox.addItem("kseniya")
        self.comboBox.addItem("xenia")
        self.comboBox.addItem("eugene")
        self.comboBox.addItem("random")

    def set_seting(self):
        privet = self.textEdit.toPlainText()
        name = self.textEdit_2.toPlainText()
        golos = self.comboBox.currentText()
        if privet != "":
            db.execute(f"""UPDATE seting_bot
                    SET Значение = '{privet}'
                    WHERE Название = 'Приветсвие'""").fetchall()
            db.commit()
        if name != "":
            db.execute(f"""UPDATE seting_bot
                    SET Значение = '{name}'
                    WHERE Название = 'Имя'""").fetchall()
            db.commit()
        if golos != "":
            db.execute(f"""UPDATE seting_bot
                    SET Значение = '{golos}'
                    WHERE Название = 'Голос'""").fetchall()
            db.commit()

    def plus_proga(self):
        cod = self.textEdit_5.toPlainText()
        adres = self.textEdit_6.toPlainText()
        if cod != "" and adres != "":
            db.execute(f"""INSERT INTO Spiski VALUES('Адреса программ', '{cod}', '{adres}')""").fetchall()
            db.commit()

    def plus_musik(self):
        genress = self.textEdit_7.toPlainText()
        creators = self.textEdit_8.toPlainText()
        names = self.textEdit_9.toPlainText()
        adress = self.textEdit_10.toPlainText()
        if genress != "" and creators != "" and names != "" and adress != "":
            db.execute(f"""INSERT INTO Music VALUES('{genress}', '{creators}', '{names}', '{adress}')""").fetchall()
            db.commit()


db = sqlite3.connect("Seting.db")
goroda = False
musik = False
genres = False
creator = False
name = False
disco = False
seting = False
pause = False
pause2 = False
trekcs = []
spi_music = []
goroda_goroda = config.goroda_igra
goroda_protivnika = []
passive_mode = False
print(numpy.__version__)
print(setuptools.__version__)
otclik = ["Я", "слушаю вас", "внимательно слушаю", "я вас слушаю"]
hour = {

}
minute = {

}
progi = {

}
mes = {

}
dni = {

}

result = db.execute("""SELECT * FROM Spiski
            WHERE Название_списка = 'Минуты'""").fetchall()
for i in result:
    minute[i[1]] = i[2]
result.clear()

result = db.execute("""SELECT * FROM Spiski
            WHERE Название_списка = 'Часы'""").fetchall()
for i in result:
    hour[i[1]] = i[2]
result.clear()

result = db.execute("""SELECT * FROM Spiski
            WHERE Название_списка = 'Адреса программ'""").fetchall()
for i in result:
    progi[i[1]] = i[2]
result.clear()

result = db.execute("""SELECT * FROM Spiski
            WHERE Название_списка = 'Месяцы'""").fetchall()
for i in result:
    mes[i[1]] = i[2]
result.clear()

result = db.execute("""SELECT * FROM Spiski
            WHERE Название_списка = 'Дни'""").fetchall()
for i in result:
    dni[i[1]] = i[2]
result.clear()

result = db.execute("""SELECT * FROM Music""").fetchall()
for i in result:
    spi_music.append(i)
result.clear()

result = db.execute("""SELECT * FROM seting_bot""").fetchall()
model_id = result[0][1]
privetstvie = result[1][1]
name = result[2][1]
if result[3][1] == "F":
    fast_with_gpu = False
else:
    fast_with_gpu = True
if result[4][1] == "F":
    put_yo = False
else:
    put_yo = True
if result[5][1] == "F":
    put_accent = False
else:
    put_accent = True
if result[9][1] == "F":
    debug_mode = False
else:
    debug_mode = True
speaker = result[6][1]
sample_rate = int(result[7][1])
language = result[8][1]
result.clear()
db.close()


def gdata():
    a = datetime.datetime.now().date()
    a = str(a).split("-")
    print(a)
    print(a[2])
    print(a[1])
    return f"{dni[int(a[2])]} {mes[int(a[1])]}"


def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))


def get_time():
    bnm = datetime.datetime.now()
    ghj = hour[bnm.strftime("%H")]
    jhg = minute[bnm.strftime("%M")]
    return f" {ghj}:{jhg}"


model = vosk.Model("model")
samplerate = 16000
device = 1
if fast_with_gpu:
    device2 = torch.device('gpu')
else:
    device2 = torch.device('cpu')
text = privetstvie
model2, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
                           model='silero_tts',
                           language=language,
                           speaker=model_id)

model2.to(device2)
q = queue.Queue()

audio = model2.apply_tts(text=privetstvie,
                         speaker=speaker,
                         sample_rate=sample_rate,
                         put_accent=put_accent,
                         put_yo=put_yo)

sd.play(audio, sample_rate)
time.sleep(len(audio) / sample_rate + 1)
sd.stop()

with sd.RawInputStream(samplerate=samplerate,
                       blocksize=8000,
                       device=device,
                       dtype="int16",
                       channels=1,
                       callback=callback):
    rec = vosk.KaldiRecognizer(model, samplerate)
    while True:
        data = q.get()
        if rec.AcceptWaveform(data):
            if debug_mode:
                print("Слушаю")

            asd = rec.Result()
            dsa = ""
            for i in asd:
                dsa += i
            asd = " ".join(dsa.split()[3:-1])
            if debug_mode:
                print(asd)

            if passive_mode:
                if name.lower() in asd:
                    passive_mode = False
                    text = random.choice(otclik)

            elif seting:
                seting = False
                app = QApplication(sys.argv)
                ex = MyWidget()
                ex.show()
                sys.exit(app.exec_())

            elif musik:
                # музыкальный плеер
                '''if genres:
                    trekcs.clear()
                    g = asd[:]
                    for i in spi_music:
                        if i[0] == g:
                            trekcs.append(i[3])
                    genres = False
                elif creator:
                    trekcs.clear()
                    g = asd[:]
                    for i in spi_music:
                        if i[1] == g:
                            trekcs.append(i[3])
                    creator = False
                elif name:
                    trekcs.clear()
                    g = asd[:]
                    for i in spi_music:
                        if i[1] == g:
                            trekcs.append(i[3])
                    name = False
                elif "жанр" in asd:
                    genres = True
                elif "исполнитель" in asd:
                    creator = True
                elif "название" in asd:
                    name = True
                elif "стоп" in asd:
                    musik = False
                else:
                    for event in pygame.event.get():
                        if STOPPED_PLAYING == event.type:'''    #бета версия плеера, работает не стабильно

                if pause:
                    pause = False
                    time.sleep(0.2)
                    pygame.mixer.music.unpause()

                elif "следующий" in asd:
                    pygame.mixer.music.stop()

                elif "что играет" in asd:
                    pygame.mixer.music.pause()
                    pause = True
                    text = f"{qwe[-2]}, исполнитель {qwe[-3]}, жанр {qwe[0]}"

                elif "пауза" in asd:
                    if not pause2:
                        pygame.mixer.music.pause()
                        pause2 = True

                elif "продолжим" in asd:
                    if pause2:
                        pygame.mixer.music.unpause()
                        pause2 = False

                for event in pygame.event.get():
                    if STOPPED_PLAYING == event.type:
                        qwe = random.choice(trekcs)
                        pygame.mixer.music.load(f"musik/{qwe[-1]}")
                        pygame.mixer.music.play()
                        del trekcs[trekcs.index(qwe)]
                        disco = True

                if "стоп" in asd:
                    musik = False
                    pygame.mixer.music.stop()

            elif "выключить" in asd:
                break

            elif "музыку" in asd:
                musik = True
                trekcs = spi_music.copy()
                qwe = random.choice(trekcs)
                pygame.mixer.music.load(f"musik/{qwe[-1]}")
                pygame.mixer.music.play()
                del trekcs[trekcs.index(qwe)]
                disco = True

            elif "настройки" in asd:
                seting = True

            elif goroda:
                f = asd[-1]
                s = ""
                if f != "":
                    for i in goroda_goroda:
                        if i[0].lower() == f.lower():
                            s = i.copy()
                            del goroda_goroda[goroda_goroda.index(i)]
                if len(goroda_goroda) == 0:
                    text = "Вы выйграли, я не знаю больше городов"
                    goroda = False
                    goroda_goroda = config.goroda_igra
                    goroda_protivnika = []
                elif asd.lower() in goroda_protivnika and asd != "":
                    text = "Было"
                elif asd == "стоп":
                    text = "Стоп игра"
                    goroda = False
                    goroda_goroda = config.goroda_igra
                    goroda_protivnika = []
                else:
                    text = s
                    goroda_protivnika.append(asd.lower())

            elif "пока" in asd:
                passive_mode = True

            elif "время" in asd:
                if debug_mode:
                    print("Обрабатываю")

                text = get_time()
                if debug_mode:
                    print("Конец Обработки")

            elif "города" in asd:
                if debug_mode:
                    print("Обрабатываю")

                goroda = True
                text = "Вы начинаете"
                if debug_mode:
                    print("Конец Обработки")

            elif "дата" in asd:
                if debug_mode:
                    print("Обрабатываю")

                text = gdata()
                if debug_mode:
                    print("Конец Обработки")

            elif "открой" in asd:

                for i in progi:
                    if i in asd:
                        subprocess.call(progi[i])
                    break

            elif name in asd:
                if debug_mode:
                    print("Обрабатываю")

                text = random.choice(otclik)
                if debug_mode:
                    print("Конец Обработки")

            else:
                text = ""
            if text != "":
                if debug_mode:
                    print("Озвучиваю")

                audio = model2.apply_tts(text=text,
                                         speaker=speaker,
                                         sample_rate=sample_rate,
                                         put_accent=put_accent,
                                         put_yo=put_yo)

                if debug_mode:
                    print("Произношу")

                sd.play(audio, sample_rate)
                time.sleep(len(audio) / sample_rate + 1)
                sd.stop()

            text = ""
# TODO поиснительная записка, выбор файла с помощью окна, презентация