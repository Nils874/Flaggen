import random
import tkinter as tk
from tkinter import Button
import fenstersettings as fs
import buttons as bt
import variablen as vb
from random import randint, choice
import bilder as bd
import anordnung_buttons as ab
import os
from PIL import Image, ImageTk
alle_laender = []
for land in os.listdir("..\\bilder"):
    f = os.path.join("..\\bilder", land)
    if os.path.isfile(f):
        landname = land[:-4]
        alle_laender.append(landname)
def flaggenrunde_start():
    for element in bt.liste_alle_buttons:
        element.place_forget()
    flaggenrunde()

def flaggenrunde():
    for element in bt.liste_alle_buttons:
        element.place_forget()
    bt.einstellungen_button.place(width=ab.einstellungen_button_width, height=ab.einstellungen_button_height, relx=ab.einstellungen_button_relx, rely=ab.einstellungen_button_rely)
    vb.laenderbutton_richtig = randint(1, 3)
    vb.aktuelles_land = choice(alle_laender)
    print(vb.aktuelles_land)
    bd.aktuelle_flagge_bild_import = ImageTk.PhotoImage(Image.open(f"..\\bilder\\{vb.aktuelles_land}.jpg"))
    bd.aktuelle_flagge_bild.config(image=bd.aktuelle_flagge_bild_import)
    bd.aktuelle_flagge_bild.pack(pady=50)
    bt.antwort_1.place(width=ab.antwort_1_width, height=ab.antwort_1_height, relx=ab.antwort_1_relx, rely=ab.antwort_1_rely)
    bt.antwort_2.place(width=ab.antwort_2_width, height=ab.antwort_2_height, relx=ab.antwort_2_relx, rely=ab.antwort_2_rely)
    bt.antwort_3.place(width=ab.antwort_3_width, height=ab.antwort_3_height, relx=ab.antwort_3_relx, rely=ab.antwort_3_rely)
    vb.erstes_falsches_land = choice(alle_laender)
    vb.zweites_falsches_land = choice(alle_laender)
    while vb.aktuelles_land == vb.erstes_falsches_land or vb.aktuelles_land == vb.zweites_falsches_land or vb.erstes_falsches_land == vb.zweites_falsches_land:
        vb.erstes_falsches_land = choice(alle_laender)
        vb.zweites_falsches_land = choice(alle_laender)
    if vb.laenderbutton_richtig == 1:
        bt.antwort_1.config(text=vb.aktuelles_land)
        bt.antwort_2.config(text=vb.erstes_falsches_land)
        bt.antwort_3.config(text=vb.zweites_falsches_land)
    elif vb.laenderbutton_richtig == 2:
        bt.antwort_1.config(text=vb.erstes_falsches_land)
        bt.antwort_2.config(text=vb.aktuelles_land)
        bt.antwort_3.config(text=vb.zweites_falsches_land)
    elif vb.laenderbutton_richtig == 3:
        bt.antwort_1.config(text=vb.erstes_falsches_land)
        bt.antwort_2.config(text=vb.zweites_falsches_land)
        bt.antwort_3.config(text=vb.aktuelles_land)


def antwort_1_ausgewaehlt():
    print("Hallo")

def antwort_2_ausgewaehlt():
    print("Hallo")

def antwort_3_ausgewahelt():
    print("Hallo")

bt.antwort_1.config(command=antwort_1_ausgewaehlt)
bt.antwort_2.config(command=antwort_2_ausgewaehlt)
bt.antwort_3.config(command=antwort_3_ausgewahelt)
bt.startbutton.config(command=flaggenrunde_start)
