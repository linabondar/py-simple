import sys
#from decimal import Decimal

#import numpy as np

def gauss_solver(n, m, matrix):
    EPS = 1e-9
    main_el = [-1] * m
    x = [0] * m

    for j in range(m):
        sel = -1
        for i in range(j, n):
            if abs(matrix[i][j]) > EPS:
                sel = i
                break
        if sel == -1:
            continue
        matrix[j], matrix[sel] = matrix[sel], matrix[j]
        main_el[j] = j

        for i in range(n):
            if i != j:
                factor = matrix[i][j] / matrix[j][j]
                for k in range(j, m + 1):
                    matrix[i][k] -= (matrix[j][k]) * factor

    # Check for inconsistency
    for k in range(n):
        if all(abs(matrix[i][k]) < EPS for k in range(m)) and abs(matrix[i][m]) > EPS:
            return "NO", []

    # Check for infinite solutions
    rank = sum(1 for k in main_el if k != -1)
    if rank < m:
        return "INF", []

    # Back-substitution
    for i in range(m - 1, -1, -1):
        if main_el[i] == -1:
            x[i] = 0
        else:
            sum_ax = sum(matrix[main_el[i]][j] * x[j] for j in range(i + 1, m))
            x[i] = (matrix[main_el[i]][m] - sum_ax) / matrix[main_el[i]][i]

    return "YES", x


def createMatrix_T(a, n, m):
    at=[]
    for j in range(m):
        at.append([0] * n)
        for i in range(n):
            at[j][i] = a[i][j]
    return at

def readMatrix_f(data):
    n = int(data[0])
    m = int(data[1])
    m_with_right = m + 1
    A = []
    b=[]

    for i in range(n):
        A.append([0] * (m))
        for j in range(m):
            A[i][j] = float(data[2 + i * (m_with_right) + j])
        b.append([float(data[2 + i * (m_with_right) + m])])

    return A, b, n, m


def multiply_matrices(A, B):
    # Get the dimensions of the matrices
    n = len(A)       # number of rows in A
    m = len(A[0])    # number of columns in A
    p = len(B[0])    # number of columns in B

    # Check if multiplication is possible
    if m != len(B):
        raise ValueError("Cannot multiply: number of columns in A must equal number of rows in B")

    # Create the result matrix (n × p) filled with zeros
    result = [[0 for _ in range(p)] for _ in range(n)]

    # Classic triple loop for matrix multiplication
    for i in range(n):
        for j in range(p):
            for k in range(m):
                result[i][j] += A[i][k] * B[k][j]

    return result


def createMatrixAb(a, b, m):
    matrix = [[0.0 for _ in range(m + 1)] for _ in range(m)]
    for i in range(m):
        for j in range(m):
           matrix[i][j]=a[i][j]
        matrix[i][m]=b[i][0]
    return matrix

def main():
    inputStr = sys.stdin.read()
    data=inputStr.split()
    A, b , n, m = readMatrix_f(data)
    At = createMatrix_T(A, n, m)

           # Метод наименьших квадратов: решаем A^T A x = A^T b
    AtA = multiply_matrices(At, A)
    Atb = multiply_matrices(At, b)
    matrix=createMatrixAb(AtA, Atb, m)
    result, solution = gauss_solver(m, m, matrix)

    if result == "YES":
        print(" ".join(f"{x:.16f}" for x in solution))


if __name__ == "__main__":
    main()

