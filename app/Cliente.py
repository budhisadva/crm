from flask import request

class Cliente():
    """docstring for Cliente."""

    def __init__(self, datos):
        self.__atr = {}
        for i in datos.keys():
            self.__atr[i] = datos.get(i)
        print(self.__atr)

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
        c, v = '', ''
        i = 0
        while i < n:
            if i != n-1:
                c += '{}, '.format(atr[i])
                v += "'{}', ".format(dicc[atr[i]])
            else:
                c += atr[i]
                v += "'{}'".format(dicc[atr[i]])
            i += 1
        return c, v

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
