from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from helpers import *
from classes import *
"""
COLORES:
Azul:"#0A3859"
Amarillo:"#FDC125"
"""
def pregame_screen(mode:str, root, canvas):
    canvas.create_image(int(canvas.cget('width'))//2,int(canvas.cget('height'))//2,anchor='center',image=imagenes.imagenes['fondos'][0]['medium'])
    widgets = list()
    canvas.create_image(int(canvas.cget('width'))/4,(int(canvas.cget('height'))//3)+50,anchor='center',image=imagenes.imagenes['entrenadores'][-1])
    dialogo = Label(root,
                    text='Selecciona a tus 3 Pokemones!',
                    anchor='center',
                    width=30,
                    height=2,
                    font=("Pocket Monk", 22, "bold"),
                    fg="#FDC125",
                    bg="#0A3859",)
    widgets.append(dialogo)
    dialogo.place(x=int(canvas.cget('width'))//8, y=int(canvas.cget('height'))*2//3)
    pokemon = StringVar(root, value='Pokemon 1')
    dropdown = ttk.Combobox(root,textvariable=pokemon)
    dropdown['values'] = tuple(['Pokemon ' + str(i) for i in range(1,11)])
    dropdown['state'] = 'readonly'
    dropdown.place(x=(int(canvas.cget('width'))*3/4)-150,y=(int(canvas.cget('height'))//2)+30)
    imagenes.last_image_id = canvas.create_image(
        (int(canvas.cget('width'))*3/4),
        (int(canvas.cget('height'))//2)-150,
        anchor='center',
        image=imagenes.imagenes['pokemones'][int(list(pokemon.get())[-1])-1])
    
    pokemon.trace_add("write", lambda x,y,z: display_personaje(canvas, int(list(pokemon.get())[-1])-1, 'pokemones', 'small'))
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
    confirmar.config(command=lambda : change_screen(root=root, canvas=canvas, widgets=widgets, func=game_screen))
    confirmar.place(x=(int(canvas.cget('width'))*3/4)+4,y=(int(canvas.cget('height'))//2)+25)
def game_screen(root, canvas):
    return
def main_screen(root, canvas):
    canvas.create_image(int(canvas.cget('width'))//2,int(canvas.cget('height'))//2,anchor='center',image=imagenes.imagenes['fondos'][0]['small'])
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
    iniciar.config(command=lambda :change_screen(root=root,canvas=canvas, widgets=widgets, func=setup_screen))
    iniciar.place(x=screen_width/2,y=screen_height*3/4, anchor='center')

def menu_screen(root, canvas):
    canvas.create_image(int(canvas.cget('width'))//2,int(canvas.cget('height'))//2,anchor='center',image=imagenes.imagenes['fondos'][0]['medium'])
    canvas.create_image(int(canvas.cget('width'))/4,(int(canvas.cget('height'))//3)+50,anchor='center',image=jugador['avatar']['medium'])
    widgets = list()
    dialogo = Label(root,
                    text='Hola ' + jugador['nombre'] + '!',
                    anchor='center',
                    width=20,
                    height=2,
                    font=("Pocket Monk", 30, "bold"),
                    fg="#FDC125",
                    bg="#0A3859",)
    widgets.append(dialogo)
    dialogo.place(x=(int(canvas.cget('width'))//8), y=(int(canvas.cget('height'))*2//3)+100)
    menu_sign = Label(root,
                    text='Menu',
                    anchor='center',
                    width=15,
                    height=2,
                    font=("Pocket Monk", 44, "bold"),
                    fg="#FDC125",
                    bg="#0A3859",)
    widgets.append(menu_sign)
    menu_sign.place(x=int(canvas.cget('width'))/2, y=int(canvas.cget('height'))//6)
    facil_button = Button(root,
                       anchor='center',
                       text='Facil',
                       width=10,
                       height=1,
                       font=("Pocket Monk", 30, "bold"),
                       fg="#FDC125",
                       bg="#0A3859",
                       relief="flat",
                       borderwidth=0,
                       highlightthickness=0,)
    widgets.append(facil_button)
    facil_button.config(command=lambda:change_screen('facil', root=root, canvas=canvas, widgets=widgets, func=pregame_screen))
    facil_button.place(x=(int(canvas.cget('width'))/2)+120, y=int(canvas.cget('height'))*3//7)
    medio_button = Button(root,
                       anchor='center',
                       text='Medio',
                       width=10,
                       height=1,
                       font=("Pocket Monk", 30, "bold"),
                       fg="#FDC125",
                       bg="#0A3859",
                       relief="flat",
                       borderwidth=0,
                       highlightthickness=0,)
    widgets.append(medio_button)
    medio_button.place(x=(int(canvas.cget('width'))/2)+120, y=int(canvas.cget('height'))*4//7)
    medio_button.config(command=lambda:change_screen('medio', root=root, canvas=canvas, widgets=widgets, func=pregame_screen))
    dificil_button = Button(root,
                       anchor='center',
                       text='Dificil',
                       width=10,
                       height=1,
                       font=("Pocket Monk", 30, "bold"),
                       fg="#FDC125",
                       bg="#0A3859",
                       relief="flat",
                       borderwidth=0,
                       highlightthickness=0,)
    widgets.append(dificil_button)
    dificil_button.place(x=(int(canvas.cget('width'))/2)+120, y=int(canvas.cget('height'))*5//7)
    dificil_button.config(command=lambda:change_screen('dificil', root=root, canvas=canvas, widgets=widgets, func=pregame_screen))



def display_personaje(canvas, index:int, personaje:str, size:str):
    global imagenes
    canvas.delete(imagenes.last_image_id)
    if personaje == 'entrenadores':
        imagen = imagenes.imagenes[personaje][index][size]
    else:
        imagen = imagenes.imagenes[personaje][index]
    imagenes.last_image_id = canvas.create_image(
        ((int(canvas.cget('width'))*3/4)),
        (int(canvas.cget('height'))//2)-150,
        anchor='center',
        image=imagen)
def setup_screen(root, canvas):
    canvas.create_image(int(canvas.cget('width'))//2,int(canvas.cget('height'))//2,anchor='center',image=imagenes.imagenes['fondos'][0]['medium'])
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
    dropdown = ttk.Combobox(root,textvariable=entrenador)
    dropdown['values'] = tuple(['Entrenador ' + str(i) for i in range(1,6)])
    dropdown['state'] = 'readonly'
    dropdown.place(x=(int(canvas.cget('width'))*3/4)-150,y=(int(canvas.cget('height'))//2)-20)
    imagenes.last_image_id = canvas.create_image(
        (int(canvas.cget('width'))*3/4),
        (int(canvas.cget('height'))//2)-150,
        anchor='center',
        image=imagenes.imagenes['entrenadores'][int(list(entrenador.get())[-1])-1]['small'])
    # TRACKEAR LOS CAMBIOS DE ENTRENADOR
    entrenador.trace_add("write", lambda x,y,z: display_personaje(canvas, (int(list(entrenador.get())[-1])-1), 'entrenadores', 'small'))
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
    confirmar.config(command=lambda :
                     player_config(root, canvas, nombre.get(), entrenador.get(), widgets) 
                     if (len(str(nombre.get())) > 3) else 
                     dialogo.config(text='tu nombre debe tener\nmas de 3 letras',
                                    width=20,
                                    height=3))
    entry.place(x=int(canvas.cget('width'))*3/4,y=(int(canvas.cget('height'))//2)-25)
    confirmar.place(x=(int(canvas.cget('width'))*3/4)+4,y=(int(canvas.cget('height'))//2)+25)



def player_config(root, canvas, nombre:str, entrenador:str, widgets:list):
    global jugador
    jugador['nombre'] = nombre
    jugador['avatar'] = imagenes.imagenes['entrenadores'][int(list(entrenador)[-1])-1]
    change_screen(root=root, canvas=canvas, widgets=widgets, func=menu_screen)





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

#COMBOBOX STYLING
style = ttk.Style()
root.option_add("*TCombobox*Listbox.font", ("Pocket Monk", 17))
root.option_add("*TCombobox*Listbox.background", "#0A3859")
root.option_add("*TCombobox*Listbox.foreground", "#FDC125")
# CANVAS
canvas = Canvas(root,width=root.winfo_screenwidth(),height=root.winfo_screenheight())
canvas.pack(fill='both', expand=True)
imagenes = Imagenes()

jugador = dict()

main_screen(root,canvas)
root.mainloop()
