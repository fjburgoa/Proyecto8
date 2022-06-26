from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import math


# ventana emergente para "Acerca De" -> círculo azul con interrogación
def AcercaDeWindow():
    messagebox.showinfo("Autor", "Javier @ Junio.2022")  # circulo azul de aviso


# ventana emergente para "Ayuda" -> triángulo amarillo de warning
def AyudaWindow():
    messagebox.showwarning("Licencia", "Para información sobre el número de Lic. Ponerse en contacto con IT")


def SalirWindow():
    # retval = messagebox.askokcancel("¿Aceptar?") #devuelve true or false
    retval = messagebox.askretrycancel("Reintentar", "No es posible cerrar el ciclo")  # devuelve true or false
    # retval = messagebox.askquestion("¿Salir?","Salir")
    '''if (retval == "yes"):
           WinBase.destroy()'''


#################################
def AbreFicheroWindow():
    selfilename = filedialog.askopenfilename(title="Selecciona Un Archivo:",
                                             initialdir="C:/Users/fjb29/PycharmProjects",
                                             filetypes=(("Python", "*.py"),
                                                        ("Excel", "*.xlsx"),
                                                        ("Texto", "*.txt"),
                                                        ("All", "*.*"),))

    print(selfilename)





