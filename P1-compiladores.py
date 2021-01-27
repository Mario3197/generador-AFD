from pip._vendor.distlib.compat import raw_input
import threading

from Estado import Estado

arregloEstados = []
alfabeto = []

# Esta función quita el salto de línea del último caracter de la línea que se esté leyendo
def quitarSaltoLinea(caracterConSaltoLinea):
    return caracterConSaltoLinea.replace('\n', '')

# Esta funcion obtiene los datos necesarios del TXT para manejarlos posteriormente, el alfabeto, estados finales, iniciales, etc.
def obtenerDatosTXT():
    archivo = open('AF3.txt', 'r')
    for index, linea in enumerate(archivo):
        if (index == 0):
            estados = linea.split(',')
            estados[len(estados) - 1] = quitarSaltoLinea(estados[len(estados) - 1])
        elif (index == 1):
            global alfabeto
            alfabeto = linea.split(',')
            alfabeto[len(alfabeto) - 1] = quitarSaltoLinea(alfabeto[len(alfabeto) - 1])
        elif (index == 2):
            estadoInicial = quitarSaltoLinea(linea)
        elif (index == 3):
            estadosFinales = linea.split(',')
            estadosFinales[len(estadosFinales) - 1] = quitarSaltoLinea(estadosFinales[len(estadosFinales) - 1])
        else:
            transicion = linea.split(',')
            estadoActual = transicion[0]
            estadoSiguiente = quitarSaltoLinea(transicion[2])
            simboloTransicion = transicion[1]
            isEstadoInicial = estadoInicial == estadoActual
            isEstadoFinal = transicion[0] in estadosFinales
            if (len(arregloEstados) == 0):
                arregloEstados.append(
                    Estado(
                        estadoActual,
                        simboloTransicion,
                        estadoSiguiente,
                        isEstadoInicial,
                        isEstadoFinal
                    )
                )
            else:
                for indexEstados, estado in enumerate(arregloEstados):
                    if (estado.estadoExiste(estadoActual)):
                        estado.insertarTransicion(simboloTransicion, estadoSiguiente)
                        break
                    if (indexEstados == len(arregloEstados) - 1):
                        arregloEstados.append(
                            Estado(
                                estadoActual,
                                simboloTransicion,
                                estadoSiguiente,
                                isEstadoInicial,
                                isEstadoFinal
                            )
                        )
                        break
    archivo.close()

def indexSiguienteEstado(estadoABuscar):
    for index, estadoActual in enumerate(arregloEstados):
        if (estadoActual.getNombreEstado() == estadoABuscar):
            return index

def evaluarMultiplesTransiciones(cadena, estadoActual, index):
    caracterAEvaluar = cadena[0]
    estadoSiguiente = estadoActual.estadoSiguienteMultiples(caracterAEvaluar, index)
    indexSiguiente = indexSiguienteEstado(estadoSiguiente)
    nuevaCadena = cadena[1:]
    evaluarCadena(nuevaCadena, arregloEstados[indexSiguiente])

def evaluarCadena(cadena, estadoActual):
    if (cadena == ''):
        if (estadoActual.getEstadoFinal()):
            print("Cadena VÁLIDA :D\n")
        else:
            print('Cadena INVÁLIDA D:\n')
        return 0

    transicionesMismoCaracter = estadoActual.transicionesConElMismoCaracter(alfabeto)
    # estadoActual.mostrarEstado()

    for transicion in transicionesMismoCaracter:
        if (transicion['cantidad'] > 1 and cadena[0] == transicion['caracter']):
            for index in range(transicion['cantidad']):
                if (index != 0):
                    hilo = threading.Thread(target = evaluarMultiplesTransiciones, args=(cadena, estadoActual, index))
                    hilo.start()

    caracterAEvaluar = cadena[0]

    estadoSiguiente = estadoActual.estadoSiguiente(caracterAEvaluar)
    indexSiguiente = indexSiguienteEstado(estadoSiguiente)
    nuevaCadena = cadena[1:]
    evaluarCadena(nuevaCadena, arregloEstados[indexSiguiente])

obtenerDatosTXT()
cadena = raw_input("Ingresa la cadena a evaluar: ")
# print(cadena)
evaluarCadena(cadena,arregloEstados[0])
"""
for estado in arregloEstados:
    estado.mostrarEstado()
"""
