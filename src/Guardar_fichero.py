#! /usr/bin/python
#!encoding: UTF-8

# Importamos el módulo "error"
import error

# Definimos una función que guardará los resultados de nuestro "experimento" en un fichero.

def save (n_inter, umbrales):
    num_iter = 10                                              #Número de comprobaciones en cada llamada a la función "error".
    f = open("fichero.txt", "w") 
    #Umbrales
    for i in range (len(t_upla_inter)):                        #"len" crea una lista con todos los índices de "t_upla_inter" (tamaño de la lista)
        f.write(str(t_upla_inter[i]) + '\n')                   #convierte la lista en una cadena para poder ser escrita en "fichero.txt"
        #error en la aproximación de cada intervalo
        for j in range (len(t_upla_umbrales)): 
            sol = error.error(10, num_iter, t_upla_umbrales)   #10=intervalos; num_iter=iteraciones; t_upla_umbrales= umbrales
            f.write(str(sol) + '\n')

   
#Si este fichero es el principal, se ejecuta el "main" -- Cuerpo del programa. 

if (__name__ == "__main__"):
    t_upla_inter = (10, 100, 1000, 10000, 100000, 1000000) 
    t_upla_umbrales = (1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-35)
    save(t_upla_inter, t_upla_umbrales)
    
