#! /usr/bin/python
#!encoding: UTF-8

#Importamos el módulo "modulo.py" que contiene la funcion "calculo" para la aproximacion de pi.
import modulo


#Definimos la funcion que calculará el porcentaje de errores.
def error (n, m, umbral):     #n = intervalos; m=iteraciones; 
    err = 0.0
    valor_pi = modulo.calculo(1)
    for j in range (m):
        aprox_pi = modulo.calculo(n)
        if (abs(aprox_pi - valor_pi) > umbral):
            err = err + 1
    return (err/m) * 100

    
#Cuerpo de comprobaciones del módulo.
if (__name__ == "__main__"):
    #Importamos la librería sys para usar de sys.argv.
    import sys
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    umbral = float(sys.argv[3])
    Sol = error(n, m, umbral)
    print ("\nHay un %.4f %% de errores.\n" %Sol)
    
