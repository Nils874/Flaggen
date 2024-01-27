import tkinter as tk
import buttons as bt
import bilder as bd
import variablen as vb
import fenstersettings as fs
from random import randint
import laenderwahl as lw



startscreen = True

def flaggenrunde():
   vb.laender_nummer = randint(1, vb.gesammt_laender_anzahl)
   zufaellige_flaggenwahl()
   bt.antwort_1.place(width=vb.antwort_1_width, height=vb.antwort_1_height, relx=vb.antwort_1_relx, rely=vb.antwort_1_rely)
   bt.antwort_2.place(width=vb.antwort_2_width, height=vb.antwort_2_height, relx=vb.antwort_2_relx, rely=vb.antwort_2_rely)
   bt.antwort_3.place(width=vb.antwort_3_width, height=vb.antwort_3_height, relx=vb.antwort_3_relx, rely=vb.antwort_3_rely)

def startmenue():
   bt.startbutton.place(width=vb)

def button_antwortenauswahl():
   if vb.laenderbutton_richtig == 1:
      bt.antwort_1.config(text=f"{vb.laendername}")
   elif vb.laenderbutton_richtig == 2:
      bt.antwort_2.config(text=f"{vb.laendername}")
   elif vb. laenderbutton_richtig == 3:
      bt.antwort_3.config(text=f"{vb.laendername}")

def antwort_3_ausgewaehlt():
   print("antwort 3 ooo ausgewählt")

bt.antwort_3.config(command=antwort_3_ausgewaehlt)


if startscreen == True:
   startscreen = False
   startmenue()

fs.root.mainloop()
