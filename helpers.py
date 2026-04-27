from tkinter import *
from PIL import Image, ImageTk
def load_images():
    logo = ImageTk.PhotoImage(Image.open("./assets/logo.png").resize((300, 300)))
    entrenadores = list()
    for i in range(1,6):
        entrenadores.append(Image.open('./assets/avatars/entrenador'+str(i)+'.png'))
        entrenadores[len(entrenadores)-1] = ImageTk.PhotoImage(entrenadores[len(entrenadores)-1].resize((150,150)))
    return
