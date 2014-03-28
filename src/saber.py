#! /usr/bin/python
#!encoding: UTF-8

#Importamos el módulo "error.py"
import error

#Función "save"
def save (n_inter, umbrales):
    num_iter = 10    #Número de comprobaciones en cada llamada a la función "error".
    #Umbrales
    for i in range (len(t_upla_inter)):   #"len" crea una lista con todos los índices de "t_upla_inter" (tamaño de la lista)
        print(str(t_upla_inter[i]))
        #error en la aproximación de cada intervalo
        for j in range (len(t_upla_umbrales)): 
            sol = error.error(10, num_iter, t_upla_umbrales)   #10=intervalos; num_iter=iteraciones; t_upla_umbrales= umbrales 
            print(str(sol))
        print('\n')         
#Llamamos a la función con un numero de intervalos, que a su vez, dentro de éste, la llama con un numero de test.


if (__name__== "__main__"):
    t_upla_inter = (10, 100, 1000, 10000, 100000, 1000000) 
    t_upla_umbrales = (1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-35)
    save(t_upla_inter, t_upla_umbrales)
