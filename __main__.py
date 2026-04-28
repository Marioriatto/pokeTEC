from tkinter import *
from PIL import Image, ImageTk
from helpers import *
def change_screen(root, canvas, widgets, func):
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
                     bg="#42B1C4",
                     relief="flat",
                     borderwidth=0,
                     highlightthickness=0,)
    widgets.append(iniciar)
    iniciar.config(command=lambda :change_screen(root,canvas, widgets, menu_screen))
    iniciar.place(x=screen_width/2,y=screen_height*3/4, anchor='center')

def menu_screen(root, canvas):
    canvas.delete('all')
    canvas.create_image(int(canvas.cget('width'))/2,int(canvas.cget('height'))/2,anchor='center',image=imagenes.imagenes['entrenadores'][-1])
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

main_screen(root,canvas)
root.mainloop()
