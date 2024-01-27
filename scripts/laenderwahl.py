import tkinter as tk
from tkinter import Button
import fenstersettings as fs
import buttons as bt
import main
import variablen as vb
import random as randint

bt.antwort_1.config(command=antwort_1_ausgewaehlt)
bt.antwort_2.config(command=antwort_2_ausgewaehlt)
bt.antwort_3.config(command=antwort_3_ausgewahelt)

def flaggenrunde():
    vb.laenderbutton_richtig = randint.random (1, 3)
    print(f"Zahl: {vb.laenderbutton_richtig}")

def antwort_1_ausgewaehlt():
    print("Hallo")

