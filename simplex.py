# PRIMER PROJECTO [ SIMPLEX ]
# Investigación Operaciones, Verano 2021

# Alejandra Lizbeth Flores García
# Luis David Hernández Reyes
# Jose Carlos Huerta García


from numpy import *
import numpy


class Simplex:
        def __init__(self, arg):
                # primero es una lista para después comvertirla en array de NUMPY
                self.tablo = []
                self.renglonObj = []
                self.columBasIni = []
                self.numFilas = 0
                self.numColums = 0

                #obtenermos areglos por cada salto de linea
                arregloInit = arg.split('\n')
        
                # quitamos espacios en blanco y obtenemos el renglon objetivo
                self.renglonObj = arregloInit[0].replace(" ", "").split(',')

                # quitamos el primer renglon 
                arregloInit.pop(0)

                # obtenemos numero filas
                self.numFilas = len(arregloInit) 
                self.numColums = len(arregloInit[0].replace(" ", "").split(','))

                i = 0
                while len(arregloInit) > 1:
                        # quitamos espacios en blanco y obtenemso los valores del renglon
                        renglonAux = arregloInit[0].replace(" ", "").split(',')

                        # insertamos la varible basica que corresponde 
                        # a este renglon(s1, s2, s3, etc...) 
                        self.columBasIni.insert(i, renglonAux[0])

                        # quitaos la variable basica para solo obtener los numeros del renglon
                        renglonAux.pop(0)

                        # Convertir lista string float a lista float 
                        numAux = [float64(idx) for idx in renglonAux]

                        #insertamos el arrelo del convertido de string a float
                        self.tablo.insert( i, numpy.array(numAux, dtype=numpy.float64) )

                        # quitamos el renglo 
                        arregloInit.pop(0)

                        i += 1

                # convertimos la lista de listas en un array tipo numpy.float64
                self.tablo = array(self.tablo, dtype=numpy.float64)

                print("numero de filas:    ", self.numFilas)
                print("numero de columnas: ", self.numColums)
                print("renglon objetivo:   ", self.renglonObj)
                print("basicas ini:        ", self.columBasIni)
                print("tablo:              \n", self.tablo)




# ================================================================
#       CONFIGURACION INICIAL

conIni = ""
conIni += "  ,    x1,        x2,     s1,     s2,     s3,     s4,     z       \n"
conIni += "S1,     1,         3,      1,      0,      0,      0,     100     \n"
conIni += "S2,     2,         8,      0,      1,      0,      0,     200     \n"
conIni += "S3,     1,         0,      0,      0,      1,      0,     24      \n"
conIni += "S4,     0,         1,      0,      0,      0,      1,     30      \n"

# ================================================================

simplex = Simplex(conIni)