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
aufgabe_richtig_ = ""

def modi_wahl():
    for i in bt.liste_alle_buttons:
        i.place_forget()
    bt.europa_flaggen_auswahl.place(width=ab.europa_flaggen_auswahl_width, height=ab.europa_flaggen_auswahl_height, relx=ab.europa_flaggen_auswahl_relx, rely=ab.europa_flaggen_auswahl_rely)
    bt.alle_flaggen_auswahl.place(width=ab.alle_flaggen_auswahl_width, height=ab.alle_flaggen_auswahl_height, relx=ab.alle_flaggen_auswahl_relx, rely=ab.alle_flaggen_auswahl_rely)

import time
for land in os.listdir("..\\bilder"):
    f = os.path.join("..\\bilder", land)
    if os.path.isfile(f):
        landname = land[:-4]
        alle_laender.append(landname)


def flaggenrunde_start():
    for element in bt.liste_alle_buttons:
        element.place_forget()
    vb.punkte = 0
    vb.aktueller_modi = "alle_laender"
    flaggenrunde()

def europa_flaggenrunde_start():
    for i in bt.liste_alle_buttons:
        i.place_forget()
    vb.punkte = 0
    print("Hallo")
    vb.aktueller_modi = "europa_laender"
    flaggenrunde()

def flaggenrunde():
    for element in bt.liste_alle_buttons:
        element.place_forget()
    if vb.hintergrundfarbe_welches_design == "white":
        for element in bt.liste_alle_buttons:
            element.config(bg="white")
    elif vb.hintergrundfarbe_welches_design == "black":
        for element in bt.liste_alle_buttons:
            element.config(bg="#393939")
    vb.land_schon_ausgewahelt = False
    bt.einstellungen_button.place(width=ab.einstellungen_button_width, height=ab.einstellungen_button_height, relx=ab.einstellungen_button_relx, rely=ab.einstellungen_button_rely)
    bt.punkte.place(width=ab.punkte_label_width, height=ab.punkte_label_height, relx=ab.punkte_label_relx, rely=ab.punkte_label_rely)
    bt.punkte.config(text=f"Punkte: {vb.punkte}")
    vb.laenderbutton_richtig = randint(1, 3)
    if vb.aktueller_modi == "alle_laender":
        vb.aktuelles_land = choice(alle_laender)
    elif vb.aktueller_modi == "europa_laender":
        vb.aktuelles_land = choice(bd.laender_europa)
    print(vb.aktuelles_land)
    bd.aktuelle_flagge_bild_import = ImageTk.PhotoImage(Image.open(f"..\\bilder\\{vb.aktuelles_land}.jpg"))
    bd.aktuelle_flagge_bild.config(image=bd.aktuelle_flagge_bild_import)
    bd.aktuelle_flagge_bild.pack(pady=50)
    bt.antwort_1.place(width=ab.antwort_1_width, height=ab.antwort_1_height, relx=ab.antwort_1_relx, rely=ab.antwort_1_rely)
    bt.antwort_2.place(width=ab.antwort_2_width, height=ab.antwort_2_height, relx=ab.antwort_2_relx, rely=ab.antwort_2_rely)
    bt.antwort_3.place(width=ab.antwort_3_width, height=ab.antwort_3_height, relx=ab.antwort_3_relx, rely=ab.antwort_3_rely)
    if vb.aktueller_modi == "alle_laender":
        vb.erstes_falsches_land = choice(alle_laender)
        vb.zweites_falsches_land = choice(alle_laender)
    elif vb.aktueller_modi == "europa_laender":
        vb.erstes_falsches_land = choice(bd.laender_europa)
        vb.zweites_falsches_land = choice(bd.laender_europa)
    while vb.aktuelles_land == vb.erstes_falsches_land or vb.aktuelles_land == vb.zweites_falsches_land or vb.erstes_falsches_land == vb.zweites_falsches_land:
        if vb.aktueller_modi == "alle laender":
            vb.erstes_falsches_land = choice(alle_laender)
            vb.zweites_falsches_land = choice(alle_laender)
        elif vb.aktueller_modi == "europa_laender":
            vb.erstes_falsches_land = choice(bd.laender_europa)
            vb.zweites_falsches_land = choice(bd.laender_europa)
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
    if vb.land_schon_ausgewahelt == True:
        print("Hallo")
    elif vb.laenderbutton_richtig == 1:
        bt.antwort_1.config(bg="green")
    elif vb.laenderbutton_richtig == 2:
        bt.antwort_1.config(bg="red")
        bt.antwort_2.config(bg="green")
        vb.antwort_1_falsch = "red"
    elif vb.laenderbutton_richtig == 3:
        bt.antwort_1.config(bg="red")
        bt.antwort_3.config(bg="green")
        vb.antwort_1_falsch = "red"
    vb.land_schon_ausgewahelt = True
    ergebnischeck()
def antwort_2_ausgewaehlt():
    if vb.land_schon_ausgewahelt == True:
        print("Hallo")
    elif vb.laenderbutton_richtig == 1:
        bt.antwort_1.config(bg="green")
        bt.antwort_2.config(bg="red")
        vb.antwort_2_falsch = "red"
    elif vb.laenderbutton_richtig == 2:
        bt.antwort_2.config(bg="green")
    elif vb.laenderbutton_richtig == 3:
        bt.antwort_2.config(bg="red")
        bt.antwort_3.config(bg="green")
        vb.antwort_2_falsch = "red"
    vb.land_schon_ausgewahelt = True
    ergebnischeck()
def antwort_3_ausgewaehlt():
    if vb.land_schon_ausgewahelt == True:
        print("Hallo")
    elif vb.laenderbutton_richtig == 1:
        bt.antwort_1.config(bg="green")
        bt.antwort_3.config(bg="red")
        vb.antwort_3_falsch = "red"
    elif vb.laenderbutton_richtig == 2:
        bt.antwort_2.config(bg="green")
        bt.antwort_3.config(bg="red")
        vb.antwort_3_falsch = "red"
    elif vb.laenderbutton_richtig == 3:
        bt.antwort_3.config(bg="green")
    vb.land_schon_ausgewahelt = True
    ergebnischeck()

def ergebnischeck():
    if vb.antwort_3_falsch != "red" and vb.antwort_2_falsch != "red" and vb.antwort_3_falsch != "red":
        vb.punkte += 1
        bt.punkte.config(text=f"Punkte: {vb.punkte}")
    else:
        bt.punkte.config(text=f"Punkte: {vb.punkte}")
    bt.naechste_aufgabe.place(width=ab.naechste_aufgabe_width, height=ab.naechste_aufgabe_height, relx=ab.naechste_aufgabe_relx, rely=ab.naechste_aufgabe_rely)
    vb.antwort_1_falsch = "green"
    vb.antwort_2_falsch = "green"
    vb.antwort_3_falsch = "green"

def noch_eine_runde():
    vb.punkte = 0
    flaggenrunde()


def runde_beenden():
    for i in bt.liste_alle_buttons:
        i.place_forget()
    bt.noch_eine_runde.place(width=ab.noch_eine_runde_width, height=ab.noch_eine_runde_height, relx=ab.noch_eine_runde_relx, rely=ab.noch_eine_runde_rely)
    bt.nach_runde_zu_startmenue.place(width=ab.nach_runde_zu_startmenue_width, height=ab.nach_runde_zu_startmenue_height, relx=ab.nach_runde_zu_startmenue_relx, rely=ab.nach_runde_zu_startmenue_rely)

#command für Buttons
bt.antwort_1.config(command=antwort_1_ausgewaehlt)
bt.antwort_2.config(command=antwort_2_ausgewaehlt)
bt.antwort_3.config(command=antwort_3_ausgewaehlt)
bt.startbutton.config(command=modi_wahl)
bt.naechste_aufgabe.config(command=flaggenrunde)
bt.europa_flaggen_auswahl.config(command=europa_flaggenrunde_start)
bt.alle_flaggen_auswahl.config(command=flaggenrunde_start)
bt.runde_beenden.config(command=runde_beenden)
bt.noch_eine_runde.config(command=noch_eine_runde)
