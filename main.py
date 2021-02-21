# Valores del Renglón Óptimo (z)
c = [5, 4, 3]
z = [5, 4, 3, 0, 0, 0]
# Matríz de valores de las restricciones
A = [[2, 3, 1], [4, 1, 2], [3, 4, 2]]
a = [[2, 3, 1, 1, 0, 0], [4, 1, 2, 0, 1, 0], [3, 4, 3, 0, 0, 1]]
# Lado derecho
b = [5, 11, 8]
d = [0, 5, 11, 8]
# Variables
tags_x = [' ', 'x1', 'x2', 'x3', 's1', 's2', 's3', 'z']
tags_y = ['s1', 's2', 's3']
# Posiciones pivot
pivot_c = 0
pivot_r = 0
# Número de variables de holgura
n_vholgura = 3


# Pasar RO a negativo
def holgura(matrix):
    for i in range(0, len(matrix)):
        matrix[i] = matrix[i] * -1

    print(f'{matrix}')

# Encontrar el más negativo del RO
def mas_negativo(matrix):
    menor = matrix[0]
    global pivot_c
    for i in range(0, len(matrix)):
        if matrix[i] < menor:
            menor = matrix[i]
            pivot_c = i

    print(f'Menor: {menor} \tPos: {pivot_c}')


def minimo(matrix):
    pivote = []
    divisiones = []
    global pivot_c, pivot_r

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j == pivot_c:
                pivote.append(matrix[i][j])
    print(pivote)

    for i in range(len(pivote)):
        div = b[i]/pivote[i]
        divisiones.append(div)

    menor=divisiones[0]
    for i in range(len(divisiones)):
        if divisiones[i]<menor:
            menor=divisiones[i]
            pivot_r=i
    print(f'Minimo={menor}\tPos:{pivot_r}\n')


def print_tableau():
    r_objetivo = ['RO']
    for i in range(0, len(z)):
        r_objetivo.append(z[i])
    r_objetivo.append(d[0])

    lineas = []
    for x in range(0, len(a)):
        linea = [tags_y[x]]
        for y in range(0, len(a[x])):
            linea.append(a[x][y])
        linea.append(b[x])
        lineas.append(linea)

    print(*tags_x, sep='\t\t')
    print(*r_objetivo, sep='\t\t')
    for line in lineas:
        print(*line, sep='\t\t')


holgura(z)
mas_negativo(z)
minimo(a)
print_tableau()
