from tkinter import *
from PIL import Image, ImageTk
import os
BASE_DIR = os.path.dirname(__file__)

class Imagenes:
    def __init__(self):
        self.load_images()
    def load_images(self):
        logo = list()
        path = os.path.join(BASE_DIR,'assets','logo.png')
        imagenCruda = Image.open(path)
        width, height = imagenCruda.size
        imagenCruda = imagenCruda.resize((width//2,height//2))
        imagenTk = ImageTk.PhotoImage(imagenCruda)
        logo.append(imagenTk)

        entrenadores = list()
        path = os.path.join(BASE_DIR,'assets','avatars')
        for i in os.listdir(path):
            imagenCruda = Image.open(os.path.join(path, i))
            width, height = imagenCruda.size
            imagenCruda = imagenCruda.resize((width//2,height//2))
            imagenTk = ImageTk.PhotoImage(imagenCruda)
            entrenadores.append(imagenTk)
        path = os.path.join(BASE_DIR, 'assets', 'presentador.png')
        imagenCruda = Image.open(path)
        width, height = imagenCruda.size
        imagenCruda = imagenCruda.resize((width//2,height//2))
        presentador = ImageTk.PhotoImage(imagenCruda)
        entrenadores.append(presentador)

        pokemones = list()
        path = os.path.join(BASE_DIR,'assets','characters')
        for i in os.listdir(path):
            imagenCruda = Image.open(os.path.join(path, i))
            width, height = imagenCruda.size
            imagenCruda = imagenCruda.resize((width//2,height//2))
            imagenTk = ImageTk.PhotoImage(imagenCruda)
            pokemones.append(imagenTk)

        self.imagenes = {'logo':[logo],
                    'entrenadores':entrenadores,
                    'pokemones':pokemones}
