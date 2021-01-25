from Transicion import Transicion

class Estado(object):
    def __init__(self, nombreEstado, caracter, estadoSiguiente,estadoInicial,estadoFinal):
        self.transiciones = []
        self.nombreEstado = nombreEstado
        self.estadoInicial = estadoInicial
        self.estadoFinal = estadoFinal
        self.transiciones.append(Transicion(caracter,estadoSiguiente))

    def estadoExiste(self,nombreEstado):
        return self.nombreEstado == nombreEstado

    def insertarTransicion(self, caracter, estadoSiguiente):
        self.transiciones.append(Transicion(caracter, estadoSiguiente))

    def transicionesConElMismoCaracter(self, alfabeto):
        caracteres = []
        for index, elementoAlfabeto in enumerate(alfabeto):
            caracteres.append({
                "caracter": elementoAlfabeto,
                "cantidad": 0
            })
            for transicion in self.transiciones:
                if (elementoAlfabeto == transicion.getCaracter()):
                    caracteres[index]['cantidad'] += 1
        return caracteres


    def mostrarEstado(self):
        print(self.nombreEstado, self.estadoInicial, self.estadoFinal)
        print('Transiciones:')
        for transicion in self.transiciones:
            transicion.mostrarTransicion()