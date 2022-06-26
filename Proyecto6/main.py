from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import math
import keyboard

from ExtraFcn import *



class Aplicacion():

    def __init__(self):

        self.raiz = Tk()   # Declara ventana de aplicación

        self.raiz.geometry('800x300')
        self.raiz.resizable(TRUE, TRUE)
        self.raiz.iconbitmap("myicon.ico")
        self.raiz.title("Ventana de aplicación")

        barraMenu = Menu(self.raiz)
        self.raiz.config(menu=barraMenu)

        archivoMenu = Menu(barraMenu, tearoff=0)
        archivoMenu.add_command(label="Nuevo", accelerator="Ctrl+N")
        archivoMenu.add_command(label="Abrir", accelerator="Ctrl+A", command=AbreFicheroWindow)
        archivoMenu.add_command(label="Cerrar", accelerator="Ctrl+C")
        archivoMenu.add_command(label="Calc. Exp", accelerator="Ctrl+E",command=self.NewWindow1)
        archivoMenu.add_command(label="Calc. X", accelerator="Ctrl+X", command=self.NewWindow2)
        archivoMenu.add_separator()
        archivoMenu.add_command(label="Guardar", underline=0)
        archivoMenu.add_command(label="Guardar Como")
        archivoMenu.add_command(label="Salir", command=SalirWindow)

        archivoEdicion = Menu(barraMenu, tearoff=0)
        archivoEdicion.add_command(label="Copiar")
        archivoEdicion.add_command(label="Pegar")
        archivoEdicion.add_command(label="Cortar")

        archivoHerramientas = Menu(barraMenu)

        archivoAyuda = Menu(barraMenu, tearoff=0)
        archivoAyuda.add_command(label="Acerca De...", command=AcercaDeWindow)
        archivoAyuda.add_command(label="Ayuda", command=AyudaWindow)

        barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
        barraMenu.add_cascade(label="Edición", menu=archivoEdicion)
        barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)
        barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)

        self.raiz.mainloop()

    def NewWindow1(self):
        ''' Construye una ventana de diálogo '''
        self.dialogo = Toplevel()   # Define una nueva ventana de diálogo
        self.dialogo.geometry("600x200")
        self.dialogo.resizable(FALSE, FALSE)

        ident = self.dialogo.winfo_id()          # Obtiene identicador de la nueva ventana
        self.dialogo.title("MiVentanaModal")

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
        StrLabelX = Label(self.dialogo, text="|x|:", textvariable=lab_x)
        StrLabelX.grid(row=1, column=1, columnspan=1)
        StrLabelY = Label(self.dialogo, text="y=e^x:", textvariable=lab_y)
        StrLabelY.grid(row=2, column=1, columnspan=1)

        # inicializa entrys
        StrX = Entry(self.dialogo, justify="center", textvariable=str_x)
        StrX.grid(row=1, column=2, columnspan=2)
        StrY = Entry(self.dialogo, justify="center", textvariable=str_y)
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
        Radiobutton(self.dialogo, text="Base e", variable=varOption, value=1).grid(row=4, column=1,  sticky="W")  # se puede poner command tb aquí dentro
        Radiobutton(self.dialogo, text="Base 10", variable=varOption, value=2).grid(row=5, column=1, sticky="W")

        # llamada directamente a la función
        StrButton1 = Button(self.dialogo, text="calcula", command=Calcula)
        StrButton1.grid(row=3, column=2, columnspan=1)
        # llamada por medio de función lambda
        StrButton2 = Button(self.dialogo, text="calcula(L)", command=lambda: CalculaL(float(str_x.get())))
        StrButton2.grid(row=3, column=3, columnspan=1)

        # ------------------------- CHECKBUTTON & PHOTO
        playa   = IntVar()
        montana = IntVar()
        ciudad  = IntVar()

        MyPhoto = PhotoImage(file="avion.png")
        MyLabel = Label(self.dialogo, image=MyPhoto, height=100, width=100).grid(row=1, column=4, rowspan=3)

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
        MyTripPlan = Label(self.dialogo, text="", textvariable=MyTextPlan).grid(row=4, column=4, sticky="W")

        Checkbutton(self.dialogo, text="Playa", onvalue=1, offvalue=0, variable=playa, command=PlanTrip).grid(row=4, column=2, sticky="W")
        Checkbutton(self.dialogo, text="Montaña", onvalue=1, offvalue=0, variable=montana, command=PlanTrip).grid(row=5, column=2, sticky="W")
        Checkbutton(self.dialogo, text="Ciudad", onvalue=1, offvalue=0, variable=ciudad, command=PlanTrip).grid(row=6, column=2, sticky="W")

        # ------------------------- Botón de cierre
        StrButton3 = Button(self.dialogo, text="CERRAR", command=self.dialogo.destroy)
        #StrButton3 = tkk.Button(self.dialogo, text="CERRAR", command=self.dialogo.destroy)
        StrButton3.grid(row=7, column=1, columnspan=2)

        self.raiz.wait_window(self.dialogo)

    def NewWindow2(self):

        #New screen
        self.dialogo = Toplevel()               # Define una nueva ventana de diálogo

        #screen resolution
        screen_width = self.dialogo.winfo_screenwidth()
        screen_height = self.dialogo.winfo_screenheight()

        self.dialogo.resizable(FALSE, FALSE)
        self.dialogo.title("Mi Segunda Ventana")
        self.dialogo.iconbitmap("myicon.ico")
        window_height = 200
        window_width  = 600
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        self.dialogo.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        ident = self.dialogo.winfo_id()          # Obtiene identicador de la nueva ventana
        print(ident)

        def key_pressed(key):
            if keyboard.is_pressed("left arrow"):
                print("<-")
            if keyboard.is_pressed("right arrow"):
                print("->")
            if keyboard.is_pressed("up arrow"):
                print("^")
            if keyboard.is_pressed("down arrow"):
                print("v")

        keyboard.on_press(key_pressed)

        VertSlide = IntVar().set(50)
        HorSlide = IntVar().set(50)

        #Slides
        Scale(self.dialogo, from_=0, to=100, tickinterval=10, \
              length=175, variable=VertSlide).place(x=10, y=10)

        Scale(self.dialogo, from_=0, to=200,tickinterval=20, \
                    variable=HorSlide,orient=HORIZONTAL,length=250).place(x=200,y=125)

        StrCloseButton = Button(self.dialogo, text="CERRAR", command=self.dialogo.destroy, width=7).place(x=540,y=170)



        self.dialogo.wait_window(self.dialogo)



def main():



    mi_app = Aplicacion()
    print(lab_x.get())
    print(lab_y.get())
    print(str_x.get())
    print(str_y.get())
    return (0)



main()
