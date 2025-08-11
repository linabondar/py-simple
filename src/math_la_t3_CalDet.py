import sys


def det_solver(n, matrix, det):
    EPS = 1e-9
    det_cur = 1

    # Поиск ненулевого ведущего элемента в текущем первом столбце
    pivot_row = -1
    for i in range(n):
        if abs(matrix[i][0]) > EPS:
            pivot_row = i
            break

    # Если ведущий элемент не найден → матрица вырождена
    if pivot_row == -1:
        return 0, matrix

    # Если нужно, меняем строки и меняем знак определителя
    if pivot_row != 0:
        matrix[0], matrix[pivot_row] = matrix[pivot_row], matrix[0]
        det_cur = -1

    # Приводим первый столбец к (matrix[0][0], 0, 0, ...)
    for i in range(1, n):
        factor = matrix[i][0] / matrix[0][0]
        for k in range(n):
            matrix[i][k] -= matrix[0][k] * factor

    # Умножаем дет на ведущий элемент
    det = det * det_cur * matrix[0][0]

    # Формируем подматрицу (размер на 1 меньше)
    matrix_cut = []
    for i in range(1, n):
        row_cut = []
        for j in range(1, n):
            row_cut.append(matrix[i][j])
        matrix_cut.append(row_cut)

    return det, matrix_cut


def readMatrix_nn(data):
    n = int(data[0])
    A = []

    for i in range(n):
        A.append([0] * n)
        for j in range(n):
            A[i][j] = int(data[1 + i * n + j])
    return A, n


def main():
    inputStr = sys.stdin.read()
    data = inputStr.split()
    matrix, n = readMatrix_nn(data)

    det = 1

    for k in range(n, 0, -1):
        det, matrix = det_solver(k, matrix, det)
        if det == 0:
            break

    print(str(int(round(det, 0))))


if __name__ == "__main__":
    main()

