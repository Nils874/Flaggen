import tkinter as tk
import buttons as bt
import bilder as bd
import variablen as vb
import fenstersettings as fs
from random import randint




startscreen = True

def flaggenrunde():
   vb.laender_nummer = randint(1, vb.gesammt_laender_anzahl)
   zufaellige_flaggenwahl()
   bt.antwort_1.place(width=vb.antwort_1_width, height=vb.antwort_1_height, relx=vb.antwort_1_relx, rely=vb.antwort_1_rely)
   bt.antwort_2.place(width=vb.antwort_2_width, height=vb.antwort_2_height, relx=vb.antwort_2_relx, rely=vb.antwort_2_rely)
   bt.antwort_3.place(width=vb.antwort_3_width, height=vb.antwort_3_height, relx=vb.antwort_3_relx, rely=vb.antwort_3_rely)

def zufaellige_flaggenwahl():
   if vb.laender_nummer == 1:
      bd.deutschlandflagge.pack(pady=100)
      vb.laendername = "Deutschland"
   elif vb.laender_nummer == 2:
      bd.afghanistanflagge.pack(pady=100)
      vb.laendername = "Afghanistan"
   button_antwortenauswahl()

def button_antwortenauswahl():
   vb.laenderbutton_richtig = randint(1, 3)
   if vb.laenderbutton_richtig == 1:
      bt.antwort_1.config(text=f"{vb.laendername}")
   elif vb.laenderbutton_richtig == 2:
      bt.antwort_2.config(text=f"{vb.laendername}")
   elif vb. laenderbutton_richtig == 3:
      bt.antwort_3.config(text=f"{vb.laendername}")

def antwort_3_ausgewaehlt():
   print("antwort 3 ausgewählt")


if startscreen == True:
   startscreen = False
   flaggenrunde()


fs.root.mainloop()