import tkinter
import pandas as pd
from tkinter import *
from tkinter import scrolledtext
from tkinter import simpledialog as sd #para askfloat...
from tkinter import messagebox         #para mensajes
from tkinter import filedialog         #para gestión de archivos
from tkinter import ttk


import matplotlib.pyplot as plt
import numpy as np
import math
import keyboard

from ExtraFcn import *

def NewWindow1():
    ''' Construye una ventana de diálogo '''
    dialogo = Toplevel()  # Define una nueva ventana de diálogo
    dialogo.geometry("600x200")
    dialogo.resizable(FALSE, FALSE)

    ident = dialogo.winfo_id()  # Obtiene identicador de la nueva ventana
    dialogo.title("MiVentanaModal")

    global lab_x, lab_y, str_x, str_y

    lab_x = StringVar()  # crea variable de tipo string para los Label
    lab_y = StringVar()  # crea variable de tipo string para los Label
    str_x = StringVar()  # crea variable de tipo string para los Entry
    str_y = StringVar()  # crea variable de tipo string para los Entry

    str_x.set("0")  # valor inicial
    str_y.set("-")
    lab_x.set("|x|=")
    lab_y.set("y=e^x:")

    inp_x = float(0)  # usa 2 variables tipo float
    out_y = float(0)

    # inicializa labels
    StrLabelX = Label(dialogo, text="|x|:", textvariable=lab_x)
    StrLabelX.grid(row=1, column=1, columnspan=1)
    StrLabelY = Label(dialogo, text="y=e^x:", textvariable=lab_y)
    StrLabelY.grid(row=2, column=1, columnspan=1)

    # inicializa entrys
    StrX = Entry(dialogo, justify="center", textvariable=str_x)
    StrX.grid(row=1, column=2, columnspan=2)
    StrY = Entry(dialogo, justify="center", textvariable=str_y)
    StrY.grid(row=2, column=2, columnspan=2)

    # funciones de evento
    def Calcula():
        inp_x = float(str_x.get())
        if (varOption.get() == 1):  # base e
            out_y = math.exp(inp_x)
            lab_y.set("y=e^x:")
        else:  # base 10
            out_y = math.pow(10, inp_x)
            lab_y.set("y=10^x:")
        str_y.set(str(out_y))

    # funciones de evento con Lambda
    def CalculaL(num):
        if (varOption.get() == 1):
            out_y = math.exp(num)
            lab_y.set("y=e^x:")
        else:
            out_y = math.pow(10, num)
            lab_y.set("y=10^x:")
        str_y.set(str(out_y))

    # ------------------------- RADIO BUTTON
    varOption = IntVar()
    varOption.set(2)  # default selection
    Radiobutton(dialogo, text="Base e", variable=varOption, value=1).grid(row=4, column=1,
                                                                          sticky="W")  # se puede poner command tb aquí dentro
    Radiobutton(dialogo, text="Base 10", variable=varOption, value=2).grid(row=5, column=1, sticky="W")

    # llamada directamente a la función
    StrButton1 = Button(dialogo, text="calcula", command=Calcula)
    StrButton1.grid(row=3, column=2, columnspan=1)
    # llamada por medio de función lambda
    StrButton2 = Button(dialogo, text="calcula(L)", command=lambda: CalculaL(float(str_x.get())))
    StrButton2.grid(row=3, column=3, columnspan=1)

    # ------------------------- CHECKBUTTON & PHOTO
    playa = IntVar()
    montana = IntVar()
    ciudad = IntVar()

    MyPhoto = PhotoImage(file="avion.png")
    MyLabel = Label(dialogo, image=MyPhoto, height=100, width=100).grid(row=1, column=4, rowspan=3)

    def PlanTrip():
        MyTextPlan.set("Mi plan es:")
        if (playa.get() == 1):
            MyTextPlan.set(MyTextPlan.get() + " PLAYA")
        if (montana.get() == 1):
            MyTextPlan.set(MyTextPlan.get() + "+MONTAÑA")
        if (ciudad.get() == 1):
            MyTextPlan.set(MyTextPlan.get() + "+CIUDAD")

    MyTextPlan = StringVar()
    MyTextPlan.set("Plan")
    MyTripPlan = Label(dialogo, text="", textvariable=MyTextPlan).grid(row=4, column=4, sticky="W")

    Checkbutton(dialogo, text="Playa", onvalue=1, offvalue=0, variable=playa, command=PlanTrip).grid(row=4,
                                                                                                     column=2,
                                                                                                     sticky="W")
    Checkbutton(dialogo, text="Montaña", onvalue=1, offvalue=0, variable=montana, command=PlanTrip).grid(row=5,
                                                                                                         column=2,
                                                                                                         sticky="W")
    Checkbutton(dialogo, text="Ciudad", onvalue=1, offvalue=0, variable=ciudad, command=PlanTrip).grid(row=6,
                                                                                                       column=2,
                                                                                                       sticky="W")

    # ------------------------- Botón de cierre
    StrButton3 = Button(dialogo, text="CERRAR", command=dialogo.destroy)
    # StrButton3 = tkk.Button(self.dialogo, text="CERRAR", command=self.dialogo.destroy)
    StrButton3.grid(row=7, column=1, columnspan=2)

    dialogo.wait_window(dialogo)
def NewWindow2():
    VertSlide = IntVar()
    HorSlide = IntVar()

    # New screen
    dialogo = Toplevel()  # Define una nueva ventana de diálogo

    # get screen resolution
    screen_width = dialogo.winfo_screenwidth()
    screen_height = dialogo.winfo_screenheight()

    # place new window in the middle of the screen
    dialogo.resizable(FALSE, FALSE)
    dialogo.title("Mi Segunda Ventana")
    dialogo.iconbitmap("myicon.ico")
    window_height = 200
    window_width = 600
    x_cordinate = int((screen_width / 2) - (window_width / 2))
    y_cordinate = int((screen_height / 2) - (window_height / 2))
    dialogo.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    ident = dialogo.winfo_id()  # Obtiene identicador de la nueva ventana
    print(ident)

    VertSlide.set(200)
    HorSlide.set(100)

    def onkeypress(event):
        if keyboard.is_pressed("left arrow"):
            HorSlideMinusOne()
            #print("<-")
        if keyboard.is_pressed("right arrow"):
            HorSlidePlusOne()
            #print("->")
        if keyboard.is_pressed("up arrow"):
            VertSlideMinusOne()
            #print("^")
        if keyboard.is_pressed("down arrow"):
            VertSlidePlusOne()
            #print("v")
    def HorSlidePlusOne():
        HorSlide.set(HorSlide.get()+1)
    def HorSlideMinusOne():
        HorSlide.set(HorSlide.get()-1)
    def VertSlidePlusOne():
        VertSlide.set(VertSlide.get()+10)
        graph()
    def VertSlideMinusOne():
        VertSlide.set(VertSlide.get()-10)
        graph()

    def graph():
        house_prices = np.random.normal(200000, VertSlide.get()*200, 5000)
        plt.hist(house_prices, 50)
        plt.show()


    #Slides & Buttons
    SclV = Scale(dialogo, from_=100, to=300, tickinterval=10, length=175, variable=VertSlide).place(x=10, y=10)
    SclH = Scale(dialogo, from_=0, to=200, tickinterval=20, length=250, variable=HorSlide, orient=HORIZONTAL).place(x=200,y=130)

    StrLeftButton = Button(dialogo, text="<<", command=HorSlideMinusOne, width=3, ).place(x=455, y=150)
    StrRightButton = Button(dialogo, text=">>", command=HorSlidePlusOne, width=3).place(x=485, y=150)
    StrDownButton = Button(dialogo, text="-1", command=VertSlideMinusOne, width=3).place(x=80, y=160)
    StrUpButton = Button(dialogo, text="+1", command=VertSlidePlusOne, width=3).place(x=110, y=160)

    StrCloseButton = Button(dialogo, text="GRAFICA", command=graph, width=7).place(x=540, y=145)
    StrCloseButton = Button(dialogo, text="CERRAR", command=dialogo.destroy, width=7).place(x=540, y=170)


    keyboard.on_press(onkeypress)

    dialogo.wait_window(dialogo)

######################## PANTALLA PRINCIPAL #########################################

self = Tk()  # Declara ventana de aplicación principal

self.geometry('800x300')
self.resizable(TRUE, TRUE)
self.iconbitmap("myicon.ico")
self.title("Ventana de aplicación")

barraMenu = Menu(self)
self.config(menu=barraMenu)

archivoMenu = Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Nuevo", accelerator="Ctrl+N")
archivoMenu.add_command(label="Abrir", accelerator="Ctrl+A", command=AbreFicheroWindow)
archivoMenu.add_command(label="Cerrar", accelerator="Ctrl+C")
archivoMenu.add_command(label="NewWindows1", accelerator="Ctrl+1", command=NewWindow1)
archivoMenu.add_command(label="NewWindows2", accelerator="Ctrl+2", command=NewWindow2)
archivoMenu.add_separator()
archivoMenu.add_command(label="Guardar", underline=0)
archivoMenu.add_command(label="Guardar Como")
archivoMenu.add_command(label="Salir", command=SalirWindow)

archivoEdicion = Menu(barraMenu, tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Pegar")
archivoEdicion.add_command(label="Cortar")

####-------- menú herramientas -------------------------------------------------------------

my_flt = DoubleVar()
my_int = IntVar()
my_str = StringVar()

my_flt.set(1.00)
my_int.set(1)
my_str.set("hola mundo")

def insert_float():
   my_flt.set(sd.askfloat("Introduce un Float", "Valor", initialvalue=0.0, minvalue=-1.0, maxvalue=999.99))

def insert_integer():
   my_int.set(sd.askinteger("Introduce un Entero", "Valor", initialvalue=0, minvalue=0, maxvalue=1000))

def insert_string():
   my_str.set(sd.askstring("Introduce un Texto", "Valor"))

def print_locals():
   print('float: %.2f' % my_flt.get())
   print('integer: %d' % my_int.get())
   print('string: %s' % my_str.get())

archivoHerramientas = Menu(barraMenu, tearoff=0)
archivoHerramientas.add_command(label="Insert Float", command=insert_float)
archivoHerramientas.add_command(label="Insert Integer", command=insert_integer)
archivoHerramientas.add_command(label="Insert String", command=insert_string)
archivoHerramientas.add_command(label="Printl Locals", command=print_locals)
####---------------------------------------------------------------------

archivoAyuda = Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Acerca De...", command=AcercaDeWindow)
archivoAyuda.add_command(label="Ayuda", command=AyudaWindow)

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edición", menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)

########## -- ----- más cosas adicionales de la pantalla ppal: ScrolledTest & Combobox

#altura height = número de líneas de texto
#anchura widht = número de caracteres por línea
text_area = scrolledtext.ScrolledText(self,wrap = tkinter.WORD,width = 60,height = 8,font = ("Times New Roman",12))
text_area.place(x=10,y=10)
text_area.focus()

text_area2 = Entry(self,width=20).place(x=500,y=100)

combo = ttk.Combobox(state="readonly",values=["Python", "C", "C++", "Java"])
combo.place(x=500,y=10)

##### ------------ PANDAS: Series & Dataframes

##----- Series
serie = pd.Series([1,2,3,4,5])
serie.name = "x"

##----- Dataframes
dataframe = pd.DataFrame({'Col1' : [1,2,3,4,5,6], 'Col2': ['a','b','c','d','f','h'] })
dataframe1 = pd.read_csv('data/iris.data',header=None)

dataframe1.head(2)
dataframe1.tail(5)

print(serie)
print(dataframe)
print(dataframe1.shape)

nombre_cols = ['long_sepalo','ancho_sepalo','long_petalo','ancho_petalo','clase']




dataframe1.columns = nombre_cols
text_area.insert(INSERT,dataframe1.head(135)) #sirve para meter datos en

#################### bucle infinito
self.mainloop()
