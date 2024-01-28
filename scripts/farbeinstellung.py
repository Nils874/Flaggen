import tkinter as tk
import buttons as bt
import variablen as vb
import anordnung_buttons
import fenstersettings as fs
import labels as lb

def hintergrundfarbe_aendern():
    #auf dunkles design schalten
    if vb.hintergrundfarbe_welches_design == "white":
        #farbeinstellungen
        fs.root.config(bg="#393939")
        bt.hintergrundfarbe_aendern.config(text="helles design")
        for button in bt.liste_alle_buttons:
            button.config(bg="#4a4a5e", fg="white")
        lb.einstellungen_background.config(bg="#393939")
        #andere befehle
        vb.hintergrundfarbe_welches_design = "black"
    #auf helles design schalten
    elif vb.hintergrundfarbe_welches_design == "black":
        #farbeinstellungen
        fs.root.config(bg="white")
        bt.hintergrundfarbe_aendern.config(text="dunkles design")
        for button in bt.liste_alle_buttons:
            button.config(bg="white", fg="black")
        lb.einstellungen_background.config(bg="white")
        #andere befehle
        vb.hintergrundfarbe_welches_design = "white"

bt.hintergrundfarbe_aendern.config(command=hintergrundfarbe_aendern)
