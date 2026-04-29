from tkinter import *
from PIL import Image, ImageTk
import os
BASE_DIR = os.path.dirname(__file__)

def change_screen(*args, root, canvas, widgets, func):
    canvas.delete('all')
    for widget in widgets:
        widget.place_forget()
    if len(args) > 0 :
        func(args, root, canvas)
    else:
        func(root, canvas)

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

        fondo = dict()
        path = os.path.join(BASE_DIR,'assets','bg.png')
        imagenCruda = Image.open(path)
        width, height = imagenCruda.size
        imagenTk = ImageTk.PhotoImage(imagenCruda)
        fondo['small'] = imagenTk
        imagenCruda = imagenCruda.resize((int(round(width*1.5)),int(round(height*1.5))))
        imagenTk = ImageTk.PhotoImage(imagenCruda)
        fondo['medium'] = imagenTk

        entrenadores = list()
        path = os.path.join(BASE_DIR,'assets','avatars')
        for i in os.listdir(path):
            fotos = dict()
            imagenAbierta = Image.open(os.path.join(path, i))
            width, height = imagenAbierta.size
            imagenCruda = imagenAbierta.resize((width//2,height//2))
            imagenTk = ImageTk.PhotoImage(imagenCruda)
            fotos['medium'] = imagenTk
            imagenCruda = imagenAbierta.resize((width//4,height//4))
            imagenTk = ImageTk.PhotoImage(imagenCruda)
            fotos['small'] = imagenTk
            entrenadores.append(fotos)
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
            if max(height,width) > 600:
                factor = int(max(imagenCruda.size)//300)
                imagenCruda = imagenCruda.resize((width//factor,height//factor))
            else:
                imagenCruda = imagenCruda.resize((width//2,height//2))
            print(imagenCruda.size)
            imagenTk = ImageTk.PhotoImage(imagenCruda)
            pokemones.append(imagenTk)

        self.imagenes = {'logo':logo,
                    'fondo':fondo,
                    'entrenadores':entrenadores,
                    'pokemones':pokemones}
    @property
    def last_image_id(self):
        return self._last_image_id
    
    @last_image_id.setter
    def last_image_id(self, value):
        self._last_image_id = value
        return