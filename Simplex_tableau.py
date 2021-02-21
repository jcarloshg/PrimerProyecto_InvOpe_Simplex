from fractions import Fraction
from prettytable import PrettyTable


class Simplex:
    def __init__(self, n_vars: int, n_restric: int, c: list, A: list, b: list, n_holgura: int):
        # Número de variables
        self.n_vars = n_vars
        # Número de restricciones
        self.n_restric = n_restric
        # Valores de z
        self.c = c
        # Matríz de valores de las restricciones
        self.A = A
        # Lado derecho
        self.b = b
        # Variables
        self.tags_x = [' ']
        self.tags_y = []
        # Posiciones pivot
        self.pivot_c = 0
        self.pivot_r = 0
        # Número de variables de holgura
        self.n_holgura = n_holgura
        # Valor óptimo
        self.z = 0

        self.__def_tags()
        self.__fo_negativa()
        self.__add_vars_holgura()

    # Definir etiquetas
    def __def_tags(self):
        for var in range(0, self.n_vars):
            self.tags_x.append(f'x{var + 1}')

        for var in range(0, self.n_holgura):
            self.tags_x.append(f's{var + 1}')
            self.tags_y.append(f's{var + 1}')

        self.tags_x.append('z')
        # print(self.tags_x)
        # print(self.tags_y)

    # Pasar coeficientes de la f.o. a negativo
    def __fo_negativa(self):
        for i in range(0, len(self.c)):
            self.c[i] = self.c[i] * -1
        # print(f'{self.c}')

    # Agregar variables de holgura
    def __add_vars_holgura(self):
        for i in range(0, self.n_holgura):
            self.c.append(0)
            for j in range(0, self.n_holgura):
                if j == i:
                    self.A[i].append(1)
                else:
                    self.A[i].append(0)
            # print(self.a[i])
        self.b.insert(0, 0)
        # print(self.c)
        # print(self.b)

    # Método para imprimir el tableau actual
    def print_tableau(self):
        # RO
        r_objetivo = ['']
        for i in range(0, len(self.c)):
            r_objetivo.append(Fraction(self.c[i]))
        r_objetivo.append(Fraction(self.b[0]))

        # R1 to Rn
        lines = []
        for x in range(0, len(self.A)):
            linea = [self.tags_y[x]]
            for y in range(0, len(self.A[x])):
                linea.append(Fraction(self.A[x][y]))
            linea.append(Fraction(self.b[x + 1]))
            lines.append(linea)

        print('\nTableau')
        table = PrettyTable(self.tags_x)
        table.add_row(r_objetivo)
        for line in lines:
            table.add_row(line)
        print(table)
        print()

    # Encontrar el más negativo del RO
    def calcular_columna_pivote(self):
        menor = 0
        hay_negativos = False
        for i in range(0, len(self.c)):
            if self.c[i] < menor:
                menor = self.c[i]
                self.pivot_c = i
                hay_negativos = True
        # print(f'Menor: {menor} \tPos: {self.pivot_c}')

        # Si hay negativos continua el simplex
        return hay_negativos

    # Calcular quién sale
    def calcular_pivote(self):
        pivote = []
        divisiones = []
        hay_positivos = False

        # Valores de la columna pivote
        for i in range(len(self.A)):
            for j in range(len(self.A[i])):
                if j == self.pivot_c:
                    pivote.append(self.A[i][j])

        # Encontrar el renglón pivote
        for i in range(0, len(pivote)):
            div = -1.0
            if pivote[i] != 0:
                div = self.b[i + 1] / pivote[i]
            divisiones.append(div)
        # print(divisiones)

        menor = divisiones[0]
        self.pivot_r = 0
        for i in range(0, len(divisiones)):
            if 0 <= divisiones[i] < menor:
                menor = divisiones[i]
                self.pivot_r = i
        # print(f'Minimo={menor}\tPos:{self.pivot_r}\n')

        # Si hay positivos continua el simplex
        if menor >= 0:
            hay_positivos = True
            print(f'Entra {self.tags_x[self.pivot_c + 1]}')
            print(f'Sale {self.tags_y[self.pivot_r]}')
            self.tags_y[self.pivot_r] = self.tags_x[self.pivot_c + 1]
        return hay_positivos

    def calcular_renglon_pivote(self):
        divisor = self.A[self.pivot_r][self.pivot_c]
        for i in range(0, len(self.A[self.pivot_r])):
            self.A[self.pivot_r][i] /= divisor
        self.b[self.pivot_r + 1] /= divisor
        # print(self.A[self.pivot_r])
        # print(Fraction(self.b[self.pivot_r+1]))

    def calcular_nuevo_ro(self):
        roa = self.c
        x = roa[self.pivot_c]
        for i in range(0, len(roa)):
            self.c[i] = self.c[i] - (x * self.A[self.pivot_r][i])
        self.b[0] = self.b[0] - (x * self.b[self.pivot_r + 1])
        # print()
        # print(self.c)
        # print(self.b[0])

    def calcular_reng_restantes(self):
        for i in range(0, self.n_restric):
            if i != self.pivot_r:
                x = self.A[i][self.pivot_c]
                for j in range(0, len(self.A[i])):
                    self.A[i][j] = self.A[i][j] - (x * self.A[self.pivot_r][j])
                self.b[i + 1] = self.b[i + 1] - (x * self.b[self.pivot_r + 1])
        # print()
        # print(self.A)
        # print(self.b)

    def realizar_simplex(self):
        es_optimo = False
        no_es_acotada = False

        while es_optimo is False:
            self.print_tableau()
            if self.calcular_columna_pivote():
                if self.calcular_pivote():
                    self.calcular_renglon_pivote()
                    self.calcular_nuevo_ro()
                    self.calcular_reng_restantes()
                else:
                    es_optimo = True
                    no_es_acotada = True
            else:
                es_optimo = True

        if no_es_acotada:
            print('La solución no está acotada.')
        else:
            print(f'El óptimo es \nz = {Fraction(self.b[0])}')
            for i in range(0, len(self.tags_y)):
                print(f'{self.tags_y[i]} = {Fraction(self.b[i+1])}')


S = Simplex(3, 3, [5, 4, 3], [[2, 3, 1], [4, 1, 2], [3, 4, 2]], [5, 11, 8], 3)
# S = Simplex(2, 4, [4, 3], [[2, 3], [-3, 2], [0, 2], [2, 1]], [6, 3, 5, 4], 4)
S = Simplex(2, 2, [2, 1], [[1, -2], [1, -1]], [1, 4], 2)
S.realizar_simplex()
'''
S.print_tableau()
S.calcular_columna_pivote()
S.calcular_pivote()
S.calcular_renglon_pivote()
S.calcular_nuevo_ro()
S.calcular_reng_restantes()

S.print_tableau()
S.calcular_columna_pivote()
S.calcular_pivote()
S.calcular_renglon_pivote()
S.calcular_nuevo_ro()
S.calcular_reng_restantes()

S.print_tableau()
'''
