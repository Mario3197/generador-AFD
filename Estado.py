from Transicion import Transicion

class Estado(object):
    def __init__(self, nombreEstado, caracter, estadoSiguiente,estadoInicial,estadoFinal):
        self.transiciones = []
        self.nombreEstado = nombreEstado
        self.estadoInicial = estadoInicial
        self.estadoFinal = estadoFinal
        self.transiciones.append(Transicion(caracter,estadoSiguiente))
        #print(self.nombreEstado, self.transiciones, self.estadoFinal)

    def estadoExiste(self,nombreEstado):
        return self.nombreEstado == nombreEstado

    def insertarTransicion(self, caracter, estadoSiguiente):
        self.transiciones.append(Transicion(caracter, estadoSiguiente))

    def mostrarEstado(self):
        print(self.nombreEstado, self.estadoInicial, self.estadoFinal)
        print('Transiciones:')
        for transicion in self.transiciones:
            transicion.mostrarTransicion()