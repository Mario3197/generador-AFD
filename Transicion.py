class Transicion:
    def __init__(self, caracter, estadoSiguiente):
        self.caracter = caracter
        self.estadoSiguiente = estadoSiguiente

    def mostrarTransicion(self):
        print(self.caracter, self.estadoSiguiente)