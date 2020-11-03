"""
Programa simple para calcular tu nota
repo [calculadora de notas](https://github.com/vichaoss/calculadoraNotas)
"""


class CalculadoraNotas:
    """
    Clase
    """

    def __init__(self):
        self.__VARIABLES = {"Puntaje Obtenido": 0.0,
                            "Puntaje Máximo": 0.0,
                            "Exigencia": 0.6,
                            "Nota Mínima": 1.0,
                            "Nota Aprobación": 4.0,
                            "Nota Máxima": 7.0,
                            "Nota Obtenida": 1.0
                            }

    def puntaje_obtenido(self):
        """
        Obtiene el puntaje obtenido
        :return: __Variables["Puntaje Obtenido"]
        """
        return self.__VARIABLES["Puntaje Obtenido"]

    def puntaje_maximo(self):
        """
        Obtiene el puntaje obtenido
        :return: __Variables["Puntaje Máximo"]
        """
        return self.__VARIABLES["Puntaje Máximo"]

    def exigencia(self):
        """
        Obtiene la exigencia
        :return: __Variables["Exigencia"]
        """
        return self.__VARIABLES["Exigencia"]

    def nota_minima(self):
        """
        Obtiene la nota minima
        :return: __Variables["Nota Mínima"]
        """
        return self.__VARIABLES["Nota Mínima"]

    def nota_aprobacion(self):
        """
        Obtiene la nota de aprobación
        :return: __Variables["Nota Aprobación"]
        """
        return self.__VARIABLES["Nota Aprobación"]

    def nota_maxima(self):
        """
        Obtiene la nota máxima
        :return: __Variables["Nota Máxima"]
        """
        return self.__VARIABLES["Nota Máxima"]

    def nota_obtenida(self):
        """
        Obtiene la nota obtenida
        :return: __Variables["Nota Obtenida"]
        """
        return self.__VARIABLES["Nota Obtenida"]

    def set_puntaje_obtenido(self, nuevo_puntaje_obtenido):
        """
        Asigna un nuevo puntaje obtenido
        :param nuevo_puntaje_obtenido:
        :return: None
        """
        self.__VARIABLES["Puntaje Obtenido"] = nuevo_puntaje_obtenido
        return

    def set_puntaje_maximo(self, nuevo_puntaje_maximo):
        """
        Asigna un nuevo puntaje maximo
        :param nuevo_puntaje_maximo:
        :return: None
        """
        self.__VARIABLES["Puntaje Máximo"] = nuevo_puntaje_maximo
        return

    def set_exigencia(self, nueva_exigencia):
        """
        Asigna una nueva exigencia
        :param nueva_exigencia:
        :return: None
        """
        self.__VARIABLES["Exigencia"] = nueva_exigencia
        return

    def set_nota_minima(self, nueva_nota_minima):
        """
        Asigna una nueva nota minima
        :param nueva_nota_minima:
        :return: None
        """
        self.__VARIABLES["Nota Mínima"] = nueva_nota_minima
        return

    def set_nota_aprobacion(self, nueva_nota_aprobacion):
        """
        Asigna una nueva nota de aprobación
        :param nueva_nota_aprobacion:
        :return: None
        """
        self.__VARIABLES["Nota Aprobación"] = nueva_nota_aprobacion
        return

    def set_nota_maxima(self, nueva_nota_maxima):
        """
        Asigna una nueva nota máxima
        :param nueva_nota_maxima:
        :return: None
        """
        self.__VARIABLES["Nota Máxima"] = nueva_nota_maxima
        return

    def set_nota_obtenida(self, nueva_nota):
        """
        Asigna una nueva nota obtenida
        :param nueva_nota:
        """
        self.__VARIABLES["Nota Obtenida"] = nueva_nota

    def calcular(self):
        """

        :return:
        """
        if self.puntaje_maximo() == 0:
            self.set_nota_obtenida(self.nota_minima())
            return self.nota_minima()

        puntajeCritico = self.puntaje_maximo() * self.exigencia()
        if self.puntaje_obtenido() < puntajeCritico:
            a = self.nota_aprobacion() - self.nota_minima()
            b = self.puntaje_obtenido() / puntajeCritico
            c = a * b
            self.set_nota_obtenida(c + self.nota_minima())
        else:
            a = self.nota_maxima() - self.nota_aprobacion()
            b = self.puntaje_obtenido() - puntajeCritico
            c = self.puntaje_maximo() * (1 - self.exigencia())
            self.set_nota_obtenida((a * (b / c)) + self.nota_aprobacion())
            if self.nota_obtenida() > self.nota_maxima():
                self.set_nota_obtenida(self.nota_maxima())
        return self.nota_obtenida()

    def getters(self):
        """
        Metodo que consolida en un diccionario los getters de la clase
        :return:
        """
        getters = {"Puntaje Obtenido": self.puntaje_obtenido(),
                   "Puntaje Máximo": self.puntaje_maximo(),
                   "Exigencia": self.exigencia(),
                   "Nota Mínima": self.nota_minima(),
                   "Nota Aprobación": self.nota_aprobacion(),
                   "Nota Máxima": self.nota_maxima(),
                   "Nota Obtenida": self.nota_obtenida()
                   }
        return getters

    pass

# calc = CalculadoraNotas()
# calc.set_puntaje_obtenido(60)
# calc.set_puntaje_maximo(100)
#
# print(calc.calcular())
