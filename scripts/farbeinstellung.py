import tkinter as tk
import buttons as bt
import variablen as vb
import anordnung_buttons
import fenstersettings as fs

def hintergrundfarbe_aendern():
    if vb.hintergrundfarbe_welches_design == "white":
        fs.root.config(bg="black")
        vb.hintergrundfarbe_welches_design = "black"
    elif vb.hintergrundfarbe_welches_design == "black":
        fs.root.config(bg="white")
        vb.hintergrundfarbe_welches_design = "white"

bt.hintergrundfarbe_aendern.config(command=hintergrundfarbe_aendern)
