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
noch_eine_runde = Button(fs.root, text="noch eine Runde")
nach_runde_zu_startmenue = Button(fs.root, text="Zum Startmenü")
programm_schliessen = Button(fs.root, text="Programm schliessen")
programm_schliessen_abschliessen = Button(fs.root, text="schliessen")
programm_schliessen_abbrechen = Button(fs.root, text="abbrechen")
flaggen_challenge = Button(fs.root, text="challenge")
flaggen_lernen = Button(fs.root, text="lernen")
welcher_modus_anzeige = Label(fs.root, text="")
streak_vorbei = Label(fs.root, text="""Du hast ein fehler
    gemacht und hast verloren""")
timer = Label(fs.root, text=f"Verbleibende Zeit")
auswertung_text_nach_runde = Label(fs.root, text="")


liste_alle_buttons = [auswertung_text_nach_runde, streak_vorbei, welcher_modus_anzeige, flaggen_challenge, flaggen_lernen, programm_schliessen_abschliessen, programm_schliessen_abbrechen, programm_schliessen, nach_runde_zu_startmenue, noch_eine_runde, runde_beenden, alle_flaggen_auswahl, europa_flaggen_auswahl, einstellungen_schliessen, punkte, naechste_aufgabe, einstellungen_button, infolabel, antwort_3, antwort_2, antwort_1, startbutton, hintergrundfarbe_aendern]