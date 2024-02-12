import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk
import fenstersettings as fs
import variablen as vb
#afghanistanflagge = Label(fs.root, image=afghanistanflagge_import)
aktuelle_flagge_bild_import = ImageTk.PhotoImage(Image.open("..\\bilder\\Ägypten.jpg"))
aktuelle_flagge_bild = Label(fs.root, image=aktuelle_flagge_bild_import)

liste_alle_laender = ["..\\bilder\\deutschland.jpg", "..\\bilder\\Bosnien und Herzegowina.jpg"]

laender_europa = ["Albanien", "Andorra", "Weißrussland", "Belgien", "Bosnien und Herzegowina", "Bulgarien", "Dänemark", "Deutschland", "Estland", "Finnland", "Frankreich", "Griechenland", "Irland", "Island", "Italien", "Kasachstan", "Kosovo", "Kroatien", "Lettland", "Lichtenstein", "Litauen", "Luxemburg", "Malta", "Moldawien", "Monaco", "Montenegro", "Niederlande", "Nordmazedonien", "Norwegen", "Österreich", "Polen", "Portugal", "Rumänien", "Russland", "San Marino", "Schweden", "Schweiz", "Serbien", "Slowakei", "Slowenien", "Spanien", "Tschechien", "Türkei", "Ukraine", "Vatikanstadt"]