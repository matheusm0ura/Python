import numpy as np

def fazer_matrix(matrix, I, J):
    for i in range(I):
        for j in range(J):
            matrix[i].append(0)
            matrix[i][j] = int(input(f'Digite {[i]}{[j]}: '))


def exibir_matrix(matrix):
    print()
    tupla = np.shape(matrix) #número de linhas e colunas são pegues.
    linha = tupla[0]
    coluna = tupla[1]
    for i in range(linha):
        for j in range(coluna):
            print(f'[{matrix[i][j]:^5}]', end='')
        print()

tamI = int(input("Linhas: "))
tamJ = int(input("Colunas: "))

matrix1 = [[] for _ in range(tamI)]
fazer_matrix(matrix1, tamI, tamJ)
exibir_matrix(matrix1)
m1= np.array(matrix1)


matrix2 = [[] for _ in range(tamI)]
fazer_matrix(matrix2, tamI, 1)
exibir_matrix(matrix2)
m2 = np.array(matrix2)

x = np.linalg.solve(m1, m2)
print()
print(x)