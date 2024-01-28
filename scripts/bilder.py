import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk
import fenstersettings as fs
import variablen as vb
#afghanistanflagge = Label(fs.root, image=afghanistanflagge_import)
aktuelle_flagge_bild_import = ImageTk.PhotoImage(Image.open("..\\bilder\\afghanistan.jpg"))
aktuelle_flagge_bild = Label(fs.root, image=aktuelle_flagge_bild_import)

liste_alle_laender = ["..\\bilder\\deutschland.jpg", "..\\bilder\\afghanistan.jpg"]
