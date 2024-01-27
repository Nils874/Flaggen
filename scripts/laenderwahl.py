import tkinter as tk
from tkinter import Button
import fenstersettings as fs
import buttons as bt
import variablen as vb
from random import randint
import bilder as bd


def flaggenrunde_start():
    for element in bt.liste_alle_elemente:
        element.place_forget()
    flaggenrunde()

def flaggenrunde():
    for element in bt.liste_alle_elemente:
        element.place_forget()
    vb.laenderbutton_richtig = randint(1, 3)
    vb.aktuelles_land = randint(bd.liste_alle_laender)

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
