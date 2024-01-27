import tkinter as tk
import buttons as bt
import variablen as vb
import anordnung_buttons
import fenstersettings as fs
vb.hintergrundfarbe_welches_design = "white"

def hintergrundfarbe_aendern():
    if vb.hintergrundfarbe_welches_design == "white":
        fs.root.config(background="black")

bt.hintergrundfarbe_aendern.config(command=hintergrundfarbe_aendern)
