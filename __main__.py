from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from helpers import *
from classes import *

def change_screen(root, canvas, widgets, func):
    canvas.delete('all')
    for widget in widgets:
        widget.place_forget()
    func(root, canvas)
def main_screen(root, canvas):
    # DRAW FELLAS
    screen_width = int(canvas.cget('width'))
    screen_height = int(canvas.cget('height'))
    widgets = list()
    canvas.create_image(int(canvas.cget('width'))/2,int(canvas.cget('height'))/2,anchor='center',image=imagenes.imagenes['logo'][0])
    iniciar = Button(root, text='Iniciar',
                     width=15,
                     height=2,
                     font=("Pocket Monk", 22, "bold"),
                     fg="#FDC125",
                     bg="#0A3859",
                     relief="flat",
                     borderwidth=0,
                     highlightthickness=0,)
    widgets.append(iniciar)
    iniciar.config(command=lambda :change_screen(root,canvas, widgets, setup_screen))
    iniciar.place(x=screen_width/2,y=screen_height*3/4, anchor='center')
def menu_screen(root, canvas):
    return
def setup_screen(root, canvas):
    global imagenes
    widgets = list()
    canvas.create_image(int(canvas.cget('width'))/4,(int(canvas.cget('height'))//3)+50,anchor='center',image=imagenes.imagenes['entrenadores'][-1])
    dialogo = Label(root,
                    text='Bienvenido a PokeTEC!\nPor favor escribe tu nombre\ny selecciona a tu entrenador!',
                    anchor='center',
                    width=30,
                    height=4,
                    font=("Pocket Monk", 22, "bold"),
                    fg="#FDC125",
                    bg="#0A3859",)
    widgets.append(dialogo)
    dialogo.place(x=int(canvas.cget('width'))//8, y=int(canvas.cget('height'))*2//3)
    nombre = StringVar(root)
    entry = Entry(root,
                  textvariable=nombre,
                  width=10,
                  font=("Pocket Monk", 22, "bold"),
                  fg="#FDC125",
                  bg="#0A3859",)
    widgets.append(entry)
    # SELECCION DE AVATAR
    entrenador = StringVar(root, value='Entrenador 1')
    dropdown = ttk.Combobox(root, textvariable=entrenador)
    dropdown['values'] = ('Entrenador' + str(i) for i in range(1,6))
    dropdown['state'] = 'readonly'
    widgets.append(dropdown)
    confirmar = Button(root,
                       text='Confirmar',
                       width=11,
                       height=1,
                       font=("Pocket Monk", 22, "bold"),
                       fg="#FDC125",
                       bg="#0A3859",
                       relief="flat",
                       borderwidth=0,
                       highlightthickness=0,)
    widgets.append(confirmar)
    confirmar.config(command=lambda :player_config(root, canvas, nombre, entrenador, widgets))
    entry.place(x=int(canvas.cget('width'))*3/4,y=(int(canvas.cget('height'))//2)-25)
    confirmar.place(x=(int(canvas.cget('width'))*3/4)+4,y=(int(canvas.cget('height'))//2)+25)

def player_config(root, canvas, nombre:str, entrenador:str, widgets:list):
    global jugador
    jugador['nombre'] = nombre
    jugador['avatar'] = imagenes.imagenes['entrenadores'][int(list(str(entrenador))[-1])]
    change_screen(root, canvas, widgets, menu_screen)
# WINDOWS SETTINGS
root = Tk()

root.title('PokeTEC')
root.minsize(600, 600)
root.resizable(width=NO, height=NO)

is_fullscreen = True
root.attributes("-fullscreen", True)

def on_and_off(root):
    global is_fullscreen
    root.attributes("-fullscreen", not is_fullscreen)
    is_fullscreen = (not is_fullscreen)
root.bind('<F11>',lambda evento : on_and_off(root))


# CANVAS
canvas = Canvas(root,width=root.winfo_screenwidth(),height=root.winfo_screenheight())
canvas.pack(fill='both', expand=True)
imagenes = Imagenes()

jugador = dict()

main_screen(root,canvas)
root.mainloop()
