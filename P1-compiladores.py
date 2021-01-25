from pip._vendor.distlib.compat import raw_input
import threading

from Estado import Estado

archivo = open('AF1.txt', 'r')

# Esta función quita el salto de línea del último caracter de la línea que se esté leyendo
def quitarSaltoLinea(caracterConSaltoLinea):
    return caracterConSaltoLinea.replace('\n','')

#Esta funcion obtiene los datos necesarios del TXT para manejarlos posteriormente, el alfabeto, estados finales, iniciales, etc.
def obtenerDatosTXT():
    arregloEstados = []
    for index, linea in enumerate(archivo):
        if(index == 0):
            estados = linea.split(',')
            estados[len(estados) - 1] = quitarSaltoLinea(estados[len(estados) - 1])
        elif(index == 1):
            alfabeto = linea.split(',')
            alfabeto[len(alfabeto) - 1] = quitarSaltoLinea(alfabeto[len(alfabeto) - 1])
        elif(index == 2):
            estadoInicial = quitarSaltoLinea(linea)
        elif(index == 3):
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
                    if(estado.estadoExiste(estadoActual)):
                        estado.insertarTransicion(simboloTransicion, estadoSiguiente)
                        break
                    if(indexEstados == len(arregloEstados) - 1):
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
    return arregloEstados

def evaluarCadena(cadena):


arregloEstados = obtenerDatosTXT()
cadena = raw_input("Ingresa la cadena a evaluar: ")
print(cadena)
"""
for estado in arregloEstados:
    estado.mostrarEstado()
"""