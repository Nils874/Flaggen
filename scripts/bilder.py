import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk
import fenstersettings as fs
deutschlandflagge_import = ImageTk.PhotoImage(Image.open("..\\bilder\\1deutschland.jpg"))
deutschlandflagge = Label(fs.root, image=deutschlandflagge_import)
afghanistanflagge_import = ImageTk.PhotoImage(Image.open("..\\bilder\\2afghanistan.jpg"))
afghanistanflagge = Label(fs.root, image=afghanistanflagge_import)
