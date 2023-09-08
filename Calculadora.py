""" 
	Proyecto: Creacion de una calculadora basica utilizando tkinter para la creacion de la interfaz grafica.
	Autor: Cesar Ramirez Hernandez.
	Correo: cesarramirezh1999@gmail.com
"""
#Cargando las librerias
from tkinter import * 
from math import *


#SE MUESTRA LA OPERACION EN LA PANTALLA.
def Ingresar_Parametros(num):
    global Cadena_Operar
    Cadena_Operar=Cadena_Operar+str(num)
    Entrada_Datos.set(Cadena_Operar)

#SE REALIZAN LAS OPERACIONES Y SE MUESTRA EL RESULTADO.
def resultado():
    global Cadena_Operar
    try:
    	Resultado=str(eval(Cadena_Operar))
    	Entrada_Datos.set(Resultado)
    except:
    	Entrada_Datos.set("Syntax Error")
    Cadena_Operar = ""

#LIMPIEZA DE PANTALLA.
def Limpiar():
    global Cadena_Operar
    Cadena_Operar=("")
    Entrada_Datos.set("Calculadora")


#Funcion principal
raiz = Tk()
raiz.title("Calculadora")

#Tamaño de la ventana 
raiz.geometry("423x500")

#COMANDO QUE PERMITE QUE LA raiz SEA CONSTANTE
raiz.resizable(width=0, height=0)

#DEFINIMOS EL COLOR DE LOS BOTONES Y DEL FONDO
raiz.configure(background="gray30")
Color_Boton_Igual=("green3")
Color_Botones=("gray20")
Color_Texto=("white");


#DEFINIMOS LAS DIMENSIONES DE LOS BOTONES
Boton_Ancho=11
Boton_Alto=3
Boton_Igual_C=16
Boton_Parent_Raiz=6

Entrada_Datos=StringVar()
Cadena_Operar=""

#SE DEFINE UNA CAJA(raiz) DONDE SE MOSTRARAN LAS OPERACIONES.
Salida=Entry(raiz,font=('arial',20,'normal'),width=24,textvariable=Entrada_Datos,bd=20,insertwidth=3,bg="cyan3",justify="right")
Salida.place(x=10,y=60)

#CREAMOS NUESTROS BOTONOS
Button(raiz,text="7",foreground=Color_Texto,bg=Color_Botones,width=Boton_Ancho,height=Boton_Alto,command=lambda:Ingresar_Parametros(7)).place(x=10,y=180)
Button(raiz,text="8",foreground=Color_Texto,bg=Color_Botones,width=Boton_Ancho,height=Boton_Alto,command=lambda:Ingresar_Parametros(8)).place(x=80,y=180)
Button(raiz,text="9",foreground=Color_Texto,bg=Color_Botones,width=Boton_Ancho,height=Boton_Alto,command=lambda:Ingresar_Parametros(9)).place(x=150,y=180)
Button(raiz,text="/",foreground=Color_Texto,bg=Color_Botones,width=Boton_Ancho,height=Boton_Alto,command=lambda:Ingresar_Parametros("/")).place(x=220,y=180)
Button(raiz,text="C",foreground=Color_Texto,bg="red",width=Boton_Igual_C,height=Boton_Alto,command=Limpiar).place(x=290,y=180)
Button(raiz,text="4",foreground=Color_Texto,bg=Color_Botones,width=Boton_Ancho,height=Boton_Alto,command=lambda:Ingresar_Parametros(4)).place(x=10,y=240)
Button(raiz,text="5",foreground=Color_Texto,bg=Color_Botones,width=Boton_Ancho,height=Boton_Alto,command=lambda:Ingresar_Parametros(5)).place(x=80,y=240)
Button(raiz,text="6",foreground=Color_Texto,bg=Color_Botones,width=Boton_Ancho,height=Boton_Alto,command=lambda:Ingresar_Parametros(6)).place(x=150,y=240)
Button(raiz,text="x",foreground=Color_Texto,bg=Color_Botones,width=Boton_Ancho,height=Boton_Alto,command=lambda:Ingresar_Parametros("*")).place(x=220,y=240)
Button(raiz,text="(",foreground=Color_Texto,bg=Color_Botones,width=Boton_Ancho,height=Boton_Alto,command=lambda:Ingresar_Parametros("(")).place(x=290,y=240)
Button(raiz,text=")",foreground=Color_Texto,bg=Color_Botones,width=Boton_Parent_Raiz,height=Boton_Alto,command=lambda:Ingresar_Parametros(")")).place(x=360,y=240)
Button(raiz,text="1",foreground=Color_Texto,bg=Color_Botones,width=Boton_Ancho,height=Boton_Alto,command=lambda:Ingresar_Parametros(1)).place(x=10,y=300)
Button(raiz,text="2",foreground=Color_Texto,bg=Color_Botones,width=Boton_Ancho,height=Boton_Alto,command=lambda:Ingresar_Parametros(2)).place(x=80,y=300)
Button(raiz,text="3",foreground=Color_Texto,bg=Color_Botones,width=Boton_Ancho,height=Boton_Alto,command=lambda:Ingresar_Parametros(3)).place(x=150,y=300)
Button(raiz,text="-",foreground=Color_Texto,bg=Color_Botones,width=Boton_Ancho,height=Boton_Alto,command=lambda:Ingresar_Parametros("-")).place(x=220,y=300)
Button(raiz,text="X^",foreground=Color_Texto,bg=Color_Botones,width=Boton_Ancho,height=Boton_Alto,command=lambda:Ingresar_Parametros("**")).place(x=290,y=300)
Button(raiz,text="√",foreground=Color_Texto,bg=Color_Botones,width=Boton_Parent_Raiz,height=Boton_Alto,command=lambda:Ingresar_Parametros("sqrt(")).place(x=360,y=300)
Button(raiz,text="0",foreground=Color_Texto,bg=Color_Botones,width=Boton_Ancho,height=Boton_Alto,command=lambda:Ingresar_Parametros(0)).place(x=10,y=360)
Button(raiz,text=".",foreground=Color_Texto,bg=Color_Botones,width=Boton_Ancho,height=Boton_Alto,command=lambda:Ingresar_Parametros(".")).place(x=80,y=360)
Button(raiz,text="%",foreground=Color_Texto,bg=Color_Botones,width=Boton_Ancho,height=Boton_Alto,command=lambda:Ingresar_Parametros("%")).place(x=150,y=360)
Button(raiz,text="+",foreground=Color_Texto,bg=Color_Botones,width=Boton_Ancho,height=Boton_Alto,command=lambda:Ingresar_Parametros("+")).place(x=220,y=360)
Button(raiz,text="=",bg=Color_Boton_Igual,width=Boton_Igual_C,height=Boton_Alto,command=resultado).place(x=290,y=360)

#SE MANDA LLAMAR LA FUNCION PARA LIMPIAR LA CAJA DE OPERACIONES Y AL IGUAL DE MANDAR LLAMAR LA FUNCION QUE PERMITE DESPLEGAR LA raiz DE TRABAJO
Limpiar()

raiz.mainloop()