"""
Programa simple para calcular tu nota
escrito por Vichaoss @
"""

def calcular_nota(puntajeObtenido=0, notaMinima=1, notaMaxima=7, exigencia=0.6, puntajeMaximo=0):
    notaMinimaAprovacion = 4
    puntajeCritico = puntajeMaximo * exigencia
    notaObtenida = 0
    if puntajeObtenido < puntajeCritico:
        notaObtenida = (((notaMinimaAprovacion - notaMinima) *
                         (puntajeObtenido / puntajeCritico)) + notaMinima)
    else:
        a = notaMaxima - notaMinimaAprovacion
        b = puntajeObtenido - puntajeCritico
        c = puntajeMaximo * (1 - exigencia)
        notaObtenida = (a * (b / c)) + notaMinimaAprovacion
        if notaObtenida > notaMaxima:
            notaObtenida = notaMaxima

    return notaObtenida


print(calcular_nota(puntajeObtenido="""Escribe tu puntaje aqui""", puntajeMaximo="""E"""))
