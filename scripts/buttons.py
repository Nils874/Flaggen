import tkinter as tk
from tkinter import Label, Button
import fenstersettings as fs

infolabel = Label(fs.root, text="Hallo!")
antwort_1 = Button(fs.root, text="")#, command=antwort_1_ausgewaehlt)
antwort_2 = Button(fs.root, text="")#, command=antwort_2_ausgewaehlt)
antwort_3 = Button(fs.root, text="") #command=antwort_3_ausgewaehlt)
startbutton = Button(fs.root, text="Start")
hintergrundfarbe_aendern = Button(fs.root, text="dunkles_design")
einstellungen_button = Button(fs.root, text="einstellungen")
einstellungen_button_background = Button(fs.root)


liste_alle_buttons = [einstellungen_button_background, einstellungen_button, infolabel, antwort_3, antwort_2, antwort_1, startbutton, hintergrundfarbe_aendern]