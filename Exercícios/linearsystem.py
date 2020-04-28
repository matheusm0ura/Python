import sympy as sym
import numpy as np


def fazer_matrix(matrix, row, column):
    for i in range(row):
        for j in range(column):
            matrix[i].append(0)
            matrix[i][j] = float(input(f'Digite {[i]}{[j]}: '))  # float para atender qualquer tipo de número.


def exibir_matrix(matrix):
    print()
    tupla = np.shape(matrix)  # número de linhas e colunas são pegues.
    linha = tupla[0]
    coluna = tupla[1]
    for i in range(linha):
        for j in range(coluna):
            print(f'[{matrix[i][j]:^5}]', end='')
        print()


tamI = int(input("Linhas: "))
tamJ = int(input("Colunas: "))
print()

matrix1 = [[] for _ in range(tamI)]
fazer_matrix(matrix1, tamI, tamJ)
exibir_matrix(matrix1)
print()

matrix2 = [[] for _ in range(tamI)]
fazer_matrix(matrix2, tamI, 1)
exibir_matrix(matrix2)
print()
new_mat = np.append(matrix1, matrix2, axis=1)

x, y, z, w, u, v = sym.symbols('x y z w u v')
sol = sym.solve_linear_system(sym.Matrix(new_mat), x, y, z, w, u, v)

valores = []
variaveis =[]

if sol is None:
    print("Sistema indeterminado (SI).")
else:
    try:
        valores = list(sol.values())
        variaveis = list(sol.keys())
        for c in range(len(valores)):
            #if not TypeError:
            valores[c] = float(valores[c])
            print(f"{variaveis[c]} = {valores[c]:.2f}")
        print("Sistema possível e determinado (SPD)")
    except TypeError: #Lança uma exceção ao tentar passar os valores para float em uma expressão simbólica.
        print(sol)
        print("Sistema possível e indeterminado (SPI)")