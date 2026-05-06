from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from helpers import *
from classes import *
from threading import Thread
from random import randint, choice, choices
"""
COLORES:
Azul:"#0A3859"
Amarillo:"#FDC125"
"""

def game(root, canvas):
    turno = "jugador"
    widgets = list()
    elementos_canvas = list()
    seleccionando_pokemon = False
    pokemon_jugador = None
    datos_jugador['pokemones'] = [Pokemon(pokemones[i]) for i in datos_jugador['pokemones']]
    datos_oponente = oponentes[choice([i for i in list(oponentes.keys()) if i != datos_jugador['avatar']])]
    datos_oponente['pokemones'] = [Pokemon(pokemones[choice(list(pokemones.keys()))]) for i in range(3)]
    
    jugador = Entrenador(datos_jugador)
    oponente = Entrenador(datos_oponente)
    pokemon_oponente = choice(oponente.pokemones)
    pokemon_jugador = choice(oponente.pokemones)
    finish_round = None
    hilo_pantalla = None
    dificultad = None
    if game_mode == "facil":
        dificultad = 0.3
    elif game_mode == "medio":
        dificultad = 0.6
    elif game_mode == "dificil":
        dificultad = 0.9
                
    def game_screen(root, canvas):
        nonlocal hilo_pantalla
        nonlocal turno
        nonlocal pokemon_jugador
        nonlocal pokemon_oponente
        nonlocal finish_round
        nonlocal seleccionando_pokemon
        nonlocal elementos_canvas
        nonlocal jugador
        nonlocal oponente
        global datos_jugador
        global datos_oponente
        seleccionando_pokemon = True
        buttons = list()
        elementos_canvas.append(canvas.create_image(
            int(canvas.cget('width'))//2,
            int(canvas.cget('height'))//2,anchor='center',
            image=imagenes.imagenes['fondos'][1]['medium']))
        ataque_button = Button(root,
                       text='',
                       width=11,
                       height=1,
                       font=("Pocket Monk", 22, "bold"),
                       fg="#FDC125",
                       bg="#0A3859",
                       relief="flat",
                       borderwidth=0,
                       highlightthickness=0,
                    )
        defensa_button = Button(root,
                       text='',
                       width=11,
                       height=1,
                       font=("Pocket Monk", 22, "bold"),
                       fg="#FDC125",
                       bg="#0A3859",
                       relief="flat",
                       borderwidth=0,
                       highlightthickness=0,
                    )
        ataque_button.config(state="disabled", command=lambda x : simular_turno([ataque_button, defensa_button], "ataque"))
        defensa_button.config(state="disabled", command=lambda x: simular_turno([ataque_button, defensa_button], "defensa"))
        widgets.append(ataque_button)
        buttons.append(ataque_button)
        widgets.append(defensa_button)
        buttons.append(defensa_button)

        vamos = canvas.create_text(
            root.winfo_width()//2,
            (root.winfo_height()//4),
            text= "",
            font=("Pocket Monk",80),
            fill="#ffffff",
            anchor='center'
        )
        elementos_canvas.append(vamos)
        jugador_vida = canvas.create_text(
            root.winfo_width()//5,
            (root.winfo_height()//5),
            text= "",
            font=("Pocket Monk",40),
            fill="#ffffff",
            anchor='center'
        )
        elementos_canvas.append(jugador_vida)
        oponente_vida = canvas.create_text(
            root.winfo_width()//5,
            (root.winfo_height()//5),
            text= "",
            font=("Pocket Monk",40),
            fill="#ffffff",
            anchor='center'
        )
        elementos_canvas.append(oponente_vida)
        elementos_canvas.append(canvas.create_image(
            int(canvas.cget('width'))//5,
            int(canvas.cget('height'))//2,anchor='center',
            image=imagenes.imagenes['entrenadores'][jugador.avatar]['small']))
        elementos_canvas.append(canvas.create_image(
            int(canvas.cget('width'))*4//5,
            int(canvas.cget('height'))//2,anchor='center',
            image=oponente.avatar['small']))
        
        def seleccionar_pokemon(root):
            nonlocal pokemon_jugador
            nonlocal seleccionando_pokemon
            pokemon_jugador = None
            pokemon_buttons = list()
            def selec(pokemon):
                nonlocal seleccionando_pokemon
                nonlocal pokemon_jugador
                seleccionando_pokemon=False
                pokemon_jugador = pokemon
            for i in range(len(jugador.pokemones)):
                pokemon_buttons.append(Button(root,
                           text=jugador.pokemones[i].nombre,
                           width=11,
                           height=1,
                           font=("Pocket Monk", 22, "bold"),
                           fg="#FDC125",
                           bg="#0A3859",
                           relief="flat",
                           borderwidth=0,
                           highlightthickness=0,
                        ))
                pokemon_buttons[-1].config(command=lambda x :selec(jugador.pokemones[i]))
                spacing = 400 // len(jugador.pokemones)
                pokemon_buttons[-1].place(x=int(canvas.cget('width'))//2, y=((int(canvas.cget('height'))//2)-spacing)+(spacing*i))
            while seleccionando_pokemon:
                if not seleccionando_pokemon:
                    break
            for butt in pokemon_buttons:
                butt.place_forget()

        def funcion(root, canvas):
            nonlocal pokemon_jugador
            nonlocal pokemon_oponente
            nonlocal ataque_button
            nonlocal defensa_button
            nonlocal finish_round
            finish_round = True
            seleccionando_pokemon = True
            pokemon_oponente = choice(oponente.pokemones)
            print(pokemon_oponente)
            while True:
                canvas.itemconfig(oponente_vida, text = "Vida: " +pokemon_oponente.vida)
                canvas.itemconfig(jugador_vida, text = "Vida: " +pokemon_jugador.vida)
                if seleccionando_pokemon:
                    seleccionar_pokemon(root)
                    print("seleccionado")
                    pokemon_oponente = choice(oponente.pokemones)
                    ataque_button.config(state='active',text=pokemon_jugador.ataques[0])
                    defensa_button.config(state='active',text=pokemon_jugador.defensas[0])
                    continue
                if finish_round:
                    if len(oponente.pokemones) == 0:
                        vamos.config(text='Gana '+jugador.nombre)
                        break
                    elif len(jugador.pokemones) == 0:
                        vamos.config(text='Gana '+oponente.nombre)
                        break
                    else:
                        pokemon_oponente = choice(oponente.pokemones)
                        ataque_button.config(state='disable',text="")
                        defensa_button.config(state='disable',text="")
                        seleccionando_pokemon = True
                        finish_round = False
                else:
                    if turno == "oponente":
                        simular_turno(buttons, choice(["atacar","defender"]))
                    
        hilo_pantalla = Thread(target=funcion, args=(root)).start()
    # FUNCION RNGsus
    def simular_turno(buttons:list, decision:str):
        nonlocal turno
        nonlocal oponente
        nonlocal jugador
        nonlocal pokemon_jugador
        nonlocal pokemon_oponente
        nonlocal finish_round
        nonlocal dificultad
        distribucion_oponente = [(1 - dificultad)/2, (1 - dificultad)/2, dificultad]
        print(distribucion_oponente)
        distribucion_jugador = [dificultad, (1 - dificultad)/2, (1 - dificultad)/2]
        print(distribucion_jugador)
        # imprimir choice(oponente.ataques)
        if turno == "jugador":
            for button in buttons:
               button.config(state="disabled")
            turno = "oponente"
            if decision == "ataque":
                pokemon_oponente.vida += (pokemon_oponente.power * pokemon_oponente.defendiendo * choices([3,6,9], weights=distribucion_oponente, k=1)[0] - (pokemon_jugador.power * choices([3,6,9],weights=distribucion_jugador,k=1)[0]))
                if pokemon_oponente.vida <= 0 :
                    oponente.pokemones.remove(pokemon_oponente)
                    pokemon_oponente.vida = 100
                    jugador.pokemones.append(pokemon_oponente)
                    pokemon_oponente = None
                    finish_round = True
                pokemon_oponente.defendiendo = 0
            elif decision == "defensa":
                pokemon_jugador.defendiendo = 1
        elif turno == "oponente":
            for button in buttons:
                button.config(state="active")
            turno = "jugador"
            if decision == "ataque":
                pokemon_jugador.vida += (pokemon_jugador.power * pokemon_jugador.defendiendo * choices([3,6,9], weights=distribucion_jugador, k=1)[0] - (pokemon_oponente.power * choices([3,6,9],weights=distribucion_oponente,k=1)[0]))
                if pokemon_jugador.vida <= 0 :
                    jugador.pokemones.remove(pokemon_jugador)
                    pokemon_jugador = None
                    finish_round = True
                pokemon_jugador.defendiendo = 0
            elif decision == "defensa":
                pokemon_oponente.defendiendo = 1
        
    Thread(target=game_screen, args=(root,canvas)).start()


def cambiar_lista_pokemones(canvas, index:int, tipo_de_personaje:str, size:str, dropdown:ttk.Combobox, label:Label, widgets, pokemon_StringVar:StringVar):
    global imagenes
    datos_jugador['pokemones'].append(index)
    if len(datos_jugador['pokemones']) < 3:
        newList = [i for i in range(0,10) if (i) not in datos_jugador['pokemones']]
        newNamesList = ['Pokemon ' + str(i+1) for i in newList]    
        dropdown['values'] = tuple(newNamesList)
        label.config(text=f'Selecciona a tu #{len(datos_jugador['pokemones']) + 1} Pokemon!')
        pokemon_StringVar.set('Pokemon ' + str(int(newList[0])+1))
        display_personaje(canvas, int(newList[0]), tipo_de_personaje, size)

    else:
        dropdown.place_forget()
        label.config(text=f'Listo!')
        canvas.delete(imagenes.last_image_id)
        imagenes.last_image_id = None
        return change_screen(root=root, canvas=canvas, widgets=widgets, func=game)
    
def pregame_screen(dificultad:str, root, canvas):
    global game_mode
    game_mode = dificultad[0]
    canvas.create_image(int(canvas.cget('width'))//2,int(canvas.cget('height'))//2,anchor='center',image=imagenes.imagenes['fondos'][0]['medium'])
    widgets = list()
    canvas.create_image(int(canvas.cget('width'))/4,(int(canvas.cget('height'))//3)+50,anchor='center',image=imagenes.imagenes['entrenadores'][-1])
    dialogo = Label(root,
                    text=f'Selecciona a tu #{1} Pokemon!',
                    anchor='center',
                    width=30,
                    height=2,
                    font=("Pocket Monk", 22, "bold"),
                    fg="#FDC125",
                    bg="#0A3859",)
    
    widgets.append(dialogo)
    dialogo.place(x=int(canvas.cget('width'))//8, y=int(canvas.cget('height'))*2//3)
    # FIRST POKEMON
    pokemon = StringVar(root, value='Pokemon 1')
    dropdown = ttk.Combobox(root,textvariable=pokemon)
    dropdown['values'] = tuple(['Pokemon ' + str(i) for i in range(1,11)])
    dropdown['state'] = 'readonly'
    dropdown.place(x=(int(canvas.cget('width'))*3/4)-150,y=(int(canvas.cget('height'))//2)+30)
    pokemon.trace_add('write',lambda x, y, z: display_personaje(canvas, int(list(pokemon.get())[-1])-1, 'pokemones', 'small'))
    imagenes.last_image_id = canvas.create_image(
        (int(canvas.cget('width'))*3/4),
        (int(canvas.cget('height'))//2)-150,
        anchor='center',
        image=imagenes.imagenes['pokemones'][int(list(pokemon.get())[-1])-1])
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
    confirmar.config(command=lambda : cambiar_lista_pokemones(canvas, int(pokemon.get()[-1])-1, 'pokemones', 'small', dropdown, label=dialogo, widgets=widgets, pokemon_StringVar=pokemon))
    confirmar.place(x=(int(canvas.cget('width'))*3/4)+4,y=(int(canvas.cget('height'))//2)+25)
"""
    PREGAME CODE FINISHES HERE
"""
def menu_screen(root, canvas):
    canvas.create_image(int(canvas.cget('width'))//2,int(canvas.cget('height'))//2,anchor='center',image=imagenes.imagenes['fondos'][0]['medium'])
    canvas.create_image(int(canvas.cget('width'))/4,(int(canvas.cget('height'))//3)+50,anchor='center',image=imagenes.imagenes['entrenadores'][datos_jugador['avatar']]['medium'])
    widgets = list()
    dialogo = Label(root,
                    text='Hola ' + datos_jugador['nombre'] + '!',
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



def display_personaje(canvas, index:int, tipo_de_personaje:str, size:str):
    global imagenes
    canvas.delete(imagenes.last_image_id)
    if tipo_de_personaje == 'entrenadores':
        imagen = imagenes.imagenes[tipo_de_personaje][index][size]
    else:
        imagen = imagenes.imagenes[tipo_de_personaje][index]
    imagenes.last_image_id = canvas.create_image(
        ((int(canvas.cget('width'))*3/4)),
        (int(canvas.cget('height'))//2)-150,
        anchor='center',
        image=imagen)


def player_config(root, canvas, nombre:str, entrenador:str, widgets:list):
    global datos_jugador
    datos_jugador['nombre'] = nombre
    datos_jugador['avatar'] = int(list(entrenador)[-1])-1
    change_screen(root=root, canvas=canvas, widgets=widgets, func=menu_screen)

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
    entrenador.trace_add("write", lambda x,y,z: display_personaje(canvas, (int(entrenador.get()[-1])-1), 'entrenadores', 'small'))
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
                     if (len(str(nombre.get())) >= 3) else 
                     dialogo.config(text='tu nombre debe tener\nmínimo 3 letras',
                                    width=20,
                                    height=3))
    entry.place(x=int(canvas.cget('width'))*3/4,y=(int(canvas.cget('height'))//2)-25)
    confirmar.place(x=(int(canvas.cget('width'))*3/4)+4,y=(int(canvas.cget('height'))//2)+25)


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

pokemones = {
    0:{ "nombre" : "BabyOil",
        "ataques" : ["Aceitar"],
        "defensas" : ["Cerrar envase"],
        "vida" : 60,
        "power":0.6},
    1:{ "nombre" : "Hamburguesa",
        "ataques" : ["Subir colesterol"],
        "defensas" : ["Quitar hambre"],
        "vida" : 67,
        "power":0.5},
    2:{ "nombre" : "Cartman",
        "ataques" : ["Chili especial"],
        "defensas" : ["Escudo humano (Butters)"],
        "vida" : 110,
        "power":0.9},
    3:{ "nombre" : "Scuba",
        "ataques" : ["Emotear"],
        "defensas" : ["Desconectar"],
        "vida" : 70,
        "power":0.6},
    4:{ "nombre" : "Drake",
        "ataques" : ["Anitta Max Win"],
        "defensas" : ["Embarrasing"],
        "vida" : 69,
        "power":0.7},
    5:{ "nombre" : "Alonso",
        "ataques" : ["Ataque de Manteca"],
        "defensas" : ["Yo nunca tuve"],
        "vida" : 80,
        "power":0.7},
    6:{ "nombre" : "Mis Notas",
        "ataques" : ["Ataque moral"],
        "defensas" : ["En revisión"],
        "vida" : 50,
        "power":0.8},
    7:{ "nombre" : "Triple T",
        "ataques" : ["Batazo"],
        "defensas" : ["Ayudame Tralalero"],
        "vida" : 80,
        "power":0.8},
    8:{ "nombre" : "Tux",
        "ataques" : ["killall"],
        "defensas" : ["sudo rm -rf /"],
        "vida" : 100,
        "power":0.6},
    9:{ "nombre" : "Wizard Cat",
        "ataques" : ["Expelliarmus"],
        "defensas" : ["Protego"],
        "vida" : 80,
        "power":0.6},
}
datos_jugador = dict()
datos_jugador['pokemones'] = list()
oponentes = {
    0:{'nombre':'King Nasir',
       'avatar':imagenes.imagenes['entrenadores'][0]
       },
    1:{'nombre':'Diddy',
       'avatar':imagenes.imagenes['entrenadores'][1]
       },
    2:{'nombre':'Charlie Kirk',
       'avatar':imagenes.imagenes['entrenadores'][2]
       },
    3:{'nombre':'La Cobra',
       'avatar':imagenes.imagenes['entrenadores'][3]
       },
    4:{'nombre':'Islam Makhachev',
       'avatar':imagenes.imagenes['entrenadores'][4]
       }
}
game_mode = ""
main_screen(root,canvas)
root.mainloop()
