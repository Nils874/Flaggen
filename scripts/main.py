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
   for i in bt.liste_alle_buttons:
      i.place_forget()
   bt.programm_schliessen.place(width=ab.programm_schliessen_width, height=ab.programm_schliessen_height, relx=ab.programm_schliessen_relx, rely=ab.programm_schliessen_rely)
   bt.startbutton.place(width=ab.startbutton_width, height=ab.startbutton_height, relx=ab.startbutton_relx, rely=ab.startbutton_rely)
   bt.hintergrundfarbe_aendern.place(width=ab.hintergrundfarbe_aendern_width, height=ab.hintergrundfarbe_aendern_height, relx=ab.hintergrundfarbe_aendern_relx, rely=ab.hintergrundfarbe_aendern_rely)

def programm_schliessen():
   for i in bt.liste_alle_buttons:
      i.place_forget()
   bt.programm_schliessen_abschliessen.place(width=ab.programm_schliessen_abschliessen_width, height=ab.programm_schliessen_abschliessen_height, relx=ab.programm_schliessen_abschliessen_relx, rely=ab.programm_schliessen_abschliessen_rely)
   bt.programm_schliessen_abbrechen.place(width=ab.programm_schliessen_abbrechen_width, height=ab.programm_schliessen_abbrechen_height, relx=ab.programm_schliessen_abbrechen_relx, rely=ab.programm_schliessen_abbrechen_rely)

def programm_schliessen_abschliessen():
   quit()

def programm_schliessen_abbrechen():
   startmenue()

if startscreen == True:
   startscreen = False
   startmenue()

#commands für Buttons
bt.nach_runde_zu_startmenue.config(command=startmenue)
bt.programm_schliessen.config(command=programm_schliessen)
bt.programm_schliessen_abschliessen.config(command=programm_schliessen_abschliessen)
bt.programm_schliessen_abbrechen.config(command=programm_schliessen_abbrechen)

fs.root.mainloop()
