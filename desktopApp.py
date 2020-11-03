"""
a
"""
from tkinter import *

from calcularNota import CalculadoraNotas

LABEL_COLUMN = 0
ENTRY_COLUMN = 1

campos = (
    "Puntaje Obtenido", "Puntaje Máximo", "Exigencia", "Nota Mínima", "Nota Aprobación", "Nota Máxima", "Nota Obtenida")

calc = CalculadoraNotas()


def calcular_en_app(lista):
    """

    :param lista:
    :return:
    """
    calc.set_puntaje_obtenido(float(lista["Puntaje Obtenido"].get()))
    calc.set_puntaje_maximo(float(lista["Puntaje Máximo"].get()))
    calc.set_exigencia(float(lista["Exigencia"].get()))
    calc.set_nota_minima(float(lista["Nota Mínima"].get()))
    calc.set_nota_aprobacion(float(lista["Nota Aprobación"].get()))
    calc.set_nota_maxima(float(lista["Nota Máxima"].get()))
    # noinspection PyUnresolvedReferences
    entradas["Nota Obtenida"].config(state=NORMAL)
    lista["Nota Obtenida"].delete(0, END)
    lista["Nota Obtenida"].insert(0, calc.calcular())
    # noinspection PyUnresolvedReferences
    entradas["Nota Obtenida"].config(state=DISABLED)
    return


def hacer_formulario(lista):
    """

    :rtype: object
    :param lista:
    :return:
    """
    diccionario = {}
    for campo in lista:
        fila = Frame(root)
        etiqueta = Label(fila, width=22, text=(campo + ": "), anchor='w')
        entrada = Entry(fila)
        entrada.insert(0, calc.getters()[campo])
        fila.pack(side=TOP, fill=X, padx=5, pady=5)
        etiqueta.pack(side=LEFT)
        entrada.pack(side=RIGHT, expand=YES, fill=X)
        diccionario[campo] = entrada
        pass

    diccionario["Nota Obtenida"].config(state=DISABLED)
    return diccionario


root = Tk()
entradas = hacer_formulario(campos)
boton_calc = Button(root, text="Calcular!", command=(lambda e=entradas: calcular_en_app(e)))
boton_calc.pack(side=LEFT, padx=5, pady=5)
root.title("Calculadora de notas")

root.mainloop()

pass
