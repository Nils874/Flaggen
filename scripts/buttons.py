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
naechste_aufgabe = Button(fs.root, text="nächste Aufgabe")
punkte = Label(fs.root, text=f"Punkte: ")
einstellungen_schliessen = Button(fs.root, text="zurück zum Spiel")
alle_flaggen_auswahl = Button(fs.root, text="Alle Flaggen")
europa_flaggen_auswahl = Button(fs.root, text="Europaflaggen")
runde_beenden = Button(fs.root, text="Runde Aufgeben")

liste_alle_buttons = [runde_beenden, alle_flaggen_auswahl, europa_flaggen_auswahl, einstellungen_schliessen, punkte, naechste_aufgabe, einstellungen_button, infolabel, antwort_3, antwort_2, antwort_1, startbutton, hintergrundfarbe_aendern]