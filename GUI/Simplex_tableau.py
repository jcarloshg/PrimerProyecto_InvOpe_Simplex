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
            self.tags_x.append(f'x{var + 1} ')

        for var in range(0, self.n_holgura):
            self.tags_x.append(f's{var + 1} ')
            self.tags_y.append(f's{var + 1} ')

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

    # Método para obtener el tableau actual
    def get_tableau(self):
        # RO
        r_objetivo = ['\t']
        for i in range(0, len(self.c)):
            r_objetivo.append(f'{Fraction(self.c[i])}\t')
        r_objetivo.append(f'{Fraction(self.b[0])}\t')

        # R1 to Rn
        lines = []
        for x in range(0, len(self.A)):
            linea = [f'{self.tags_y[x]}\t']
            for y in range(0, len(self.A[x])):
                linea.append(f'{Fraction(self.A[x][y])}\t')
            linea.append(f'{Fraction(self.b[x + 1])}\t')
            lines.append(linea)

        header = []
        for i in range(0, len(self.tags_x)):
            header.append(f'{self.tags_x[i]}\t')

        table = PrettyTable(header)
        table.add_row(r_objetivo)
        for line in lines:
            table.add_row(line)

        # return table.get_html_string()
        return table.get_string()

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
            if pivote[i] != 0 and self.b[i+1] != 0:
                div = self.b[i + 1] / pivote[i]
            divisiones.append(div)
        # print(divisiones)

        float_max = 1.7976931348623157e+308
        menor = float_max
        self.pivot_r = 0
        for i in range(0, len(divisiones)):
            if 0 <= divisiones[i] < menor:
                menor = divisiones[i]
                self.pivot_r = i
        # print(f'Minimo={menor}\tPos:{self.pivot_r}\n')

        # Si hay positivos continua el simplex
        if menor >= 0 and menor != float_max:
            hay_positivos = True

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
        # print(b[0])

    def calcular_reng_restantes(self):
        degenerada = False
        for i in range(0, self.n_restric):
            if i != self.pivot_r:
                x = self.A[i][self.pivot_c]
                for j in range(0, len(self.A[i])):
                    self.A[i][j] = self.A[i][j] - (x * self.A[self.pivot_r][j])
                self.b[i + 1] = self.b[i + 1] - (x * self.b[self.pivot_r + 1])
        # print()
        # print(self.A)
        for k in range(1, len(self.b)):
            if self.b[k] == 0:
                degenerada = True

        return degenerada

    def realizar_simplex(self):
        es_optimo = False
        no_es_acotada = False
        es_degenerada = False

        while es_optimo is False:
            self.print_tableau()
            if self.calcular_columna_pivote():
                if self.calcular_pivote():
                    print(f'Entra {self.tags_x[self.pivot_c + 1]}')
                    print(f'Sale {self.tags_y[self.pivot_r]}')
                    self.tags_y[self.pivot_r] = self.tags_x[self.pivot_c + 1]
                    self.calcular_renglon_pivote()
                    self.calcular_nuevo_ro()
                    if self.calcular_reng_restantes():
                        es_degenerada = True
                        # es_optimo = True
                else:
                    es_optimo = True
                    no_es_acotada = True
            else:
                es_optimo = True

        if no_es_acotada:
            print('La solución no está acotada.')
        elif es_degenerada:
            # self.print_tableau()
            print('La solución es temporalmente degenerada.')
            print(f'El óptimo es \nz = {Fraction(self.b[0])}')
            for i in range(0, len(self.tags_y)):
                print(f'{self.tags_y[i]} = {Fraction(self.b[i + 1])}')
        else:
            print(f'El óptimo es \nz = {Fraction(self.b[0])}')
            for i in range(0, len(self.tags_y)):
                print(f'{self.tags_y[i]} = {Fraction(self.b[i + 1])}')

    def realizar_simplex_gui(self):
        resultado = []
        es_optimo = False
        no_es_acotada = False
        es_degenerada = False
        idx = 1

        while es_optimo is False:
            resultado.append(f'Tableau {idx}')
            resultado.append(self.get_tableau())
            resultado.append('')
            idx += 1
            if self.calcular_columna_pivote():
                if self.calcular_pivote():
                    resultado.append(f'Entra {self.tags_x[self.pivot_c + 1]}')
                    resultado.append(f'Sale {self.tags_y[self.pivot_r]}')
                    self.tags_y[self.pivot_r] = self.tags_x[self.pivot_c + 1]
                    resultado.append('')
                    self.calcular_renglon_pivote()
                    self.calcular_nuevo_ro()
                    if self.calcular_reng_restantes():
                        es_degenerada = True
                        # es_optimo = True
                else:
                    es_optimo = True
                    no_es_acotada = True
            else:
                es_optimo = True

        if no_es_acotada:
            resultado.append('La solución no está acotada.')
        elif es_degenerada:
            """resultado.append(f'Tableau {idx}')
            resultado.append(self.get_tableau())
            resultado.append('')"""
            resultado.append('La solución es degenerada.')
            resultado.append('El óptimo es')
            resultado.append(f'z = {Fraction(self.b[0])}')
            for i in range(0, len(self.tags_y)):
                resultado.append(f'{self.tags_y[i]} = {Fraction(self.b[i + 1])}')
        else:
            resultado.append('El óptimo es')
            resultado.append(f'z = {Fraction(self.b[0])}')
            for i in range(0, len(self.tags_y)):
                resultado.append(f'{self.tags_y[i]} = {Fraction(self.b[i + 1])}')

        return resultado


def main():
    """
    n_variables = int(input('Número de variables: '))
    n_restricciones = int(input('Número de variables: '))

    z = []
    print('\nFunción Objetivo Z = ')
    for i in range(0, n_variables):
        value = int(input(f'Valor de x{i+1} = '))
        z.append(value)
    print()
    # print(z)

    a = []
    for j in range(0, n_restricciones):
        print(f'Restricción {j+1}')
        renglones = []
        for k in range(0, n_variables):
            valor = int(input(f'Valor de x{k+1} = '))
            renglones.append(valor)
        a.append(renglones)
        print()
    # print(a)

    l_derecho = []
    print('Lado derecho')
    for x in range(0, n_restricciones):
        value = int(input(f'Valor de x{x+1} = '))
        l_derecho.append(value)
    print()
    """

    # S = Simplex(n_variables, n_restricciones, z, a, l_derecho, n_restricciones)
    # S = Simplex(3, 3, [5, 4, 3], [[2, 3, 1], [4, 1, 2], [3, 4, 2]], [5, 11, 8], 3)
    # S = Simplex(2, 4, [4, 3], [[2, 3], [-3, 2], [0, 2], [2, 1]], [6, 3, 5, 4], 4)
    # S = Simplex(2, 2, [2, 1], [[1, -1], [2, -1]], [1, 4], 2)
    # S = Simplex(2, 3, [2, 1], [[4, 3], [4, 1], [4, -1]], [12, 8, 8], 3)
    # S.realizar_simplex()


if __name__ == '__main__':
    main()
