import tkinter as tk
import buttons as bt
import bilder as bd
import variablen as vb
import fenstersettings as fs
from random import randint
import laenderwahl as lw
import anordnung_buttons as ab
import variablen as vb
import farbeinstellung as fe
import einstellungen
from tkinter import Menu, Label

startscreen = True


def startmenue():
   bt.startbutton.place(width=ab.startbutton_width, height=ab.startbutton_height, relx=ab.startbutton_relx, rely=ab.startbutton_rely)
   bt.hintergrundfarbe_aendern.place(width=ab.hintergrundfarbe_aendern_width, height=ab.hintergrundfarbe_aendern_height, relx=ab.hintergrundfarbe_aendern_relx, rely=ab.hintergrundfarbe_aendern_rely)

if startscreen == True:
   startscreen = False
   startmenue()

fs.root.mainloop()
