# PRIMER PROJECTO [ SIMPLEX ]
# Investigación Operaciones, Verano 2021

# Alejandra Lizbeth Flores García
# Luis David Hernández Reyes
# Jose Carlos Huerta García


from numpy import *
import numpy

tablo = []
renglonObj = []
columBasIni = []

def stringToTablo(arg):
        #obtenermos areglos por cada salto de linea
        arregloInit = arg.split('\n')
        
        # quitamos espacios en blanco y obtenemos el renglon objetivo
        renglonObj = arregloInit[0].replace(" ", "").split(',')

        # quitamos el primer renglon 
        arregloInit.pop(0)

        # obtenemos numero filas
        numFilas = len(arregloInit) 
        numColums = len(arregloInit[0].replace(" ", "").split(',')) 

        # primero es una lista para después comvertirla en array de NUMPY
        tablo = []
        
        i = 0
        while len(arregloInit) > 1:
                # quitamos espacios en blanco y obtenemso los valores del renglon
                renglonAux = arregloInit[0].replace(" ", "").split(',')

                # insertamos la varible basica que corresponde 
                # a este renglon(s1, s2, s3, etc...) 
                columBasIni.insert(i, renglonAux[0])

                # quitaos la variable basica para solo obtener los numeros del renglon
                renglonAux.pop(0)

                # Convertir lista string float a lista float 
                numAux = [float64(idx) for idx in renglonAux]

                #insertamos el arrelo del convertido de string a float
                tablo.insert(
                        i,
                        numpy.array(numAux, dtype=numpy.float64)
                        )

                # quitamos el renglo 
                arregloInit.pop(0)

                i += 1

        # convertimos la lista de listas en un array tipo numpy.float64
        tablo = array(tablo, dtype=numpy.float64)

                
        print("numero de filas:    ", numFilas)
        print("numero de columnas: ", numColums)
        print("renglon objetivo:   ", renglonObj)
        print("basicas ini:        ", columBasIni)
        print("tablo:              \n", tablo)


# ================================
# ================================
#       CONFIGURACION INICIAL

conIni = ""
conIni += "  ,    x1,        x2,     s1,     s2,     s3,     s4,     z       \n"
conIni += "S1,     1,         3,      1,      0,      0,      0,     100     \n"
conIni += "S2,     2,         8,      0,      1,      0,      0,     200     \n"
conIni += "S3,     1,         0,      0,      0,      1,      0,     24      \n"
conIni += "S4,     0,         1,      0,      0,      0,      1,     30      \n"

stringToTablo(conIni)

# ================================
# ================================
