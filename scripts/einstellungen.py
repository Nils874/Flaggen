import tkinter as tk
import buttons as bt
import anordnung_buttons as ab
import bilder as bd
import laenderwahl as lw
import labels as lb
einstellungen_offen_ = False

def einstellungen_oeffnen():
    for i in bt.liste_alle_buttons:
        i.place_forget()
    bd.aktuelle_flagge_bild.pack_forget()
    einstellungen_offen_ = True
    bt.hintergrundfarbe_aendern.place(width=ab.hintergrundfarbe_aendern_width, height=ab.hintergrundfarbe_aendern_height, relx=0.43, rely=0.3)
    bt.einstellungen_schliessen.place(width=ab.einstellungen_schliessen_width, height=ab.einstellungen_schliessen_height, relx=ab.einstellungen_schliessen_relx, rely=ab.einstellungen_schliessen_rely)
    bt.runde_beenden.place(width=ab.runde_beenden_width, height=ab.runde_beenden_height, relx=ab.runde_beenden_relx, rely=ab.runde_beenden_rely)


def einstellungen_schliessen():
    for i in bt.liste_alle_buttons:
        i.place_forget()
    bd.aktuelle_flagge_bild.pack(pady=50)
    bt.antwort_1.place(width=ab.antwort_1_width, height=ab.antwort_1_height, relx=ab.antwort_1_relx, rely=ab.antwort_1_rely)
    bt.antwort_2.place(width=ab.antwort_2_width, height=ab.antwort_2_height, relx=ab.antwort_2_relx, rely=ab.antwort_2_rely)
    bt.antwort_3.place(width=ab.antwort_3_width, height=ab.antwort_3_height, relx=ab.antwort_3_relx, rely=ab.antwort_3_rely)
    bd.aktuelle_flagge_bild.config(image=bd.aktuelle_flagge_bild_import)
    bt.einstellungen_button.place(width=ab.einstellungen_button_width, height=ab.einstellungen_button_height, relx=ab.einstellungen_button_relx, rely=ab.einstellungen_button_rely)

#commands für Buttons
bt.einstellungen_schliessen.config(command=einstellungen_schliessen)
bt.einstellungen_button.config(command=einstellungen_oeffnen)