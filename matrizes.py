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


def subMatrix(matrix, matrix2):
    tamI = len(matrix)
    tamI = len(matrix2)
    C = [[] for _ in range(tamI)]
    for i in range(tamI):
        for j in range(tamJ):
            C[i].append(0)
            C[i][j] = matrix[i][j] - matrix2[i][j]
    print(f"{' M 1 - M 2 ':=^30}")
    exibir_matrix(C)


def somaMatrix(matrix, matrix2):
    tamI = len(matrix)
    tamI = len(matrix2)
    C = [[] for _ in range(tamI)]
    for i in range(tamI):
        for j in range(tamJ):
            C[i].append(0)
            C[i][j] = matrix[i][j] + matrix2[i][j]
    print(f"{' M 1 + M 2 ':=^30}")
    exibir_matrix(C)


def mult_matrix(matrix1, matrix2):
    tupla = np.shape(matrix1)
    tupla2 = np.shape(matrix2)
    linha1 = tupla[0]
    coluna1 = tupla[1]
    coluna2 = tupla2[1]
    C = [[] for _ in range(linha1)]
    for i in range(linha1):
        for j in range(coluna2):
            C[i].append(0)
            for k in range(coluna1):
                C[i][j] += matrix1[i][k] * matrix2[k][j]
    print(f"{' M 1 X M 2 ':=^30}")
    exibir_matrix(C)



while True:
    print(f"{' OPERAÇÕES COM MATRIZES ':=^50}")
    print("""[1] Somar
[2] Subtrair
[3] Multiplicar matrizes
[4] Multiplicar matriz por um número""")

    op = str(input("Opção: "))
    while op not in "1234":
        op = str(input("Opção: "))

    if op == "1":
        tamI = int(input('Linhas: '))
        tamJ = int(input('Colunas: '))

        if tamI == tamJ:
            matriz = [[] for _ in range(tamI)]  # Faz uam lista de listas de acordo com o número digitado em 'tamI'.
            matrix2 = [[] for _ in range(tamI)]

            print(f"{' MATRIX 1 ':=^30} ")
            fazer_matrix(matriz, tamI, tamJ)
            exibir_matrix(matriz)

            print(f"{' MATRIX 2 ':=^30} ")
            fazer_matrix(matrix2, tamI, tamJ)
            exibir_matrix(matrix2)

            somaMatrix(matriz, matrix2)

        else:
            print("Impossivel soma ou subtrair matrizes com tamanhos diferentes")

    elif op == "2":
        tamI = int(input('Linhas: '))
        tamJ = int(input('Colunas: '))

        if tamI == tamJ:
            matriz = [[] for _ in range(tamI)]  # Faz uam lista de listas de acordo com o número digitado em 'tamI'.
            matrix2 = [[] for _ in range(tamI)]

            print(f"{' MATRIX 1 ':=^30} ")
            fazer_matrix(matriz, tamI, tamJ)
            exibir_matrix(matriz)

            print(f"{' MATRIX 2 ':=^30} ")
            fazer_matrix(matrix2, tamI, tamJ)
            exibir_matrix(matrix2)

            subMatrix(matriz, matrix2)

        else:
            print("Impossivel soma ou subtrair matrizes com tamanhos diferentes")

    elif op == "3":
        tamI1 = int(input("Linhas matrix 1: "))
        tamJ1 = int(input("Colunas matrix 1: "))
        tamI2 = int(input("Linhas matrix 2: "))
        tamJ2 = int(input("Colunas matrix 2: "))
        print()

        if tamJ1 == tamI2:
            matrix1 = [[] for _ in range(tamI1)]
            matrix2 = [[] for _ in range(tamI2)]

            print(f"{' MATRIX 1 ':=^30} ")
            fazer_matrix(matrix1, tamI1, tamJ2)
            exibir_matrix(matrix1)

            print(f"{' MATRIX 2 ':=^30} ")
            fazer_matrix(matrix2, tamI2, tamJ2)
            exibir_matrix(matrix2)

            mult_matrix(matrix1, matrix2)

        else:
            print("O número de LINHAS da matrix 1 precisa ser igual o número de COLUNAS da matrix 2")

    elif op == "4":
        tamI = int(input('Linhas: '))
        tamJ = int(input('Colunas: '))
        num = int(input("Número: "))

        matrix = [[] for _ in range(tamI)]

        fazer_matrix(matrix, tamI, tamJ)
        for i in range(tamI):
            for j in range(tamJ):
                matrix[i][j] *= num
        print()
        print(f"Matriz X {num}")
        exibir_matrix(matrix)

    print()
    op2 = str(input("Gostaria de fazer outra operação [S/N]: ")).strip().upper()
    while op2 not in "SN":
        op2 = str(input("Gostaria de fazer outra operação [S/N]: "))
    if op2 == "N":
        break
