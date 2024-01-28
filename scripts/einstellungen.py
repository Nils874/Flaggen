import tkinter as tk
import buttons as bt
import anordnung_buttons as ab
import labels as lb

def einstellungen_oeffnen():
    bt.hintergrundfarbe_aendern.place(width=ab.hintergrundfarbe_aendern_width, height=ab.hintergrundfarbe_aendern_height, relx=0.43, rely=0.3)
    #bt.einstellungen_button_background.place(width=ab.einstellungen_background_width, height=ab.einstellungen_background_height, relx=ab.einstellungen_background_relx, rely=ab.einstellungen_background_rely)

bt.einstellungen_button.config(command=einstellungen_oeffnen)