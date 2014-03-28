#! /usr/bin/python
#!encoding: UTF-8


# Importamos el módulo "error"
import error


# Definimos una función que guardará los resultados de nuestro problema en un fichero.

def save (name, n_inter, umbrales):
    num_iter = 10                                              #Número de comprobaciones en cada llamada a la función "error".
    f = open(name, "w")
    for i in range (len(t_upla_inter)):                       #"len" crea una lista con todos los indices de "l" (tamaño de la lista) 
        f.write(str(t_upla_inter[i]) + '\n')                  #"str" convierte la lista en una cadena para poder escribirlo en el nuevo fichero "name".
        for j in range (len(t_upla_umbrales)):
            sol = error.error(10, num_iter, t_upla_umbrales)
            f.write(str(sol) + '\n') 
            
   
# Cuerpo de comprobaciones del módulo.

if (__name__ == "__main__"):
    t_upla_inter = (10, 100, 1000, 10000, 100000, 1000000) 
    t_upla_umbrales = (1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-35)
    name = "fichero.txt"
    save(name, t_upla_inter, t_upla_umbrales)
    

    
    # la funcion save no la entiendo ¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿???????????????????
    # ¿¿¿¿¿¿cierro el fichero name????????
    