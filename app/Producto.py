from flask import request

class Producto():
    """docstring for Producto."""

    def __init__(self):
        self.__atr = {}

    def setByRequest(self, datos):
        """
        Configura los valores de los atributos.
        Arg:
        datos : [(c,v)] donde c : Columa, v : str
        """
        for i in list(datos):
            self.__atr[i] = datos[i]
        return 0

    def insertQuery(self):
        dicc = self.__atr
        atr = list(dicc)
        n = len(atr)
        columnas = ''
        valores = ''
        i = 0
        while i < n:
            if i != n-1:
                columnas += atr[i]+', '
                valores += "'"+dicc[atr[i]]+"', "
            else:
                columnas += atr[i]
                valores += "'"+dicc[atr[i]]+"'"
            i += 1
        return columnas, valores

    def updateQuery(self):
        dicc = self.__atr
        atr = list(dicc)
        n = len(atr)
        w = ''
        i = 0
        while i < n:
            if i != n-1:
                w += "{} = '{}', ".format(atr[i], dicc[atr[i]])
            else:
                w += "{} = '{}'".format(atr[i], dicc[atr[i]])
            i += 1
        return w

    def getAtr(self):
        return self.__atr
