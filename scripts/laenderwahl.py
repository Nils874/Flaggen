import tkinter as tk
from tkinter import Button
import fenstersettings as fs
import buttons as bt
import main
import variablen as vb

bt.antwort_1.config(command=antwort_1_ausgewaehlt)
bt.antwort_2.config(command=antwort_2_ausgewaehlt)
bt.antwort_3.config(command=antwort_3_ausgewahelt)

def antwort_1_ausgewaehlt():
    vb.laenderbutton_richtig = randint(1, 3)

if vb.startscreen == True:
    vb.startscreen = False
    flaggenrunde()