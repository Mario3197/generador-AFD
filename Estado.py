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

    def getNombreEstado(self):
        return self.nombreEstado

    def getEstadoFinal(self):
        return self.estadoFinal

    def insertarTransicion(self, caracter, estadoSiguiente):
        self.transiciones.append(Transicion(caracter, estadoSiguiente))

    def estadoSiguiente(self, caracter):
        for transicion in self.transiciones:
            if (transicion.getCaracter() == caracter):
                return transicion.estadoSiguiente

    def estadoSiguienteMultiples(self, caracter, transicionBuscada):
        transicionesMismoCaracter = 0
        for index, transicion in enumerate(self.transiciones):
            caracterEvaluado = transicion.getCaracter()
            if (caracterEvaluado == caracter and (index - transicionesMismoCaracter) == transicionBuscada):
                return transicion.estadoSiguiente
            else:
                if (caracterEvaluado == caracter):
                    transicionesMismoCaracter += 1

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