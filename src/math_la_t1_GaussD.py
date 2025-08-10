import sys
from decimal import Decimal

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
                    matrix[i][k] -= matrix[j][k] * factor

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


def readMatrix(data):
    n = int(data[0])
    m = int(data[1])
    m_with_right = m + 1
    matrix = []

    for i in range(n):
        matrix.append([0] * (m_with_right))
        for j in range(m_with_right):
            matrix[i][j] = Decimal(data[2 + i * (m_with_right) + j])


    return matrix, n, m

def main():

    inputStr = sys.stdin.read()

    data=inputStr.split()
    matrix, n, m = readMatrix(data)
    result, solution = gauss_solver(n, m, matrix)
    print(result)

    if result == "YES":
        print(" ".join(f"{x:.16f}" for x in solution))

if __name__ == "__main__":
    main()

