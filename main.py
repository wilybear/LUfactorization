import numpy as np
from math import gcd
from fractions import Fraction
def printMatrix(matrix):
    print("[", end="")
    for i in range(len(matrix)):
        if i != 0:
            print(" [",end="")
        else:
            print("[",end="")
        for j in range(len(matrix[i])):
            print("%-6s"%str(matrix[i][j]), end="\t")
        if i == len(matrix)-1:
            print("]]")
        else:
            print("]")
if __name__ == "__main__":
    row = int(input("행을 입력해주세요: "))
    col = int(input("열을 입력해주세요: "))
    entries = list(map(int, input("component를 일렬로 space로 구별하여 입력해주세요(정수만): ").split()))
    # 수업에서 다룬 matrix 들
    # 3 6 -3 6 15 -5 -1 -2 6
    # 1 -3 -2 0 1 -2 1 -1 2 -4 3 2
    matrix = np.array(entries, dtype=Fraction).reshape(row, col)

    print(matrix)
    # 분수가 나올 수 있으므로 type 을 Fraction 으로
    # Doolittle algorithm 사용
    U = np.zeros((row,col),dtype=Fraction)
    L = np.identity(row,dtype=Fraction )

    # i = 0, j = 0 일때의 초기값들
    for c in range(col):
        U[0][c] = matrix[0][c]
    for r in range(row):
        L[r][0] = Fraction(matrix[r][0], U[0][0])

    for i in range(1,row):
        for k in range(i, col):
            total = 0
            for j in range(i):
                total += L[i][j] * U[j][k]
            U[i][k] = matrix[i][k] - Fraction(total)
        for k in range(i, row):
            if k != i:
                total = 0
                for j in range(i):
                    total += L[k][j] * U[j][i]
                L[k][i] = Fraction(matrix[k][i] - Fraction(total), U[i][i])
    # 결과 출력
    print("L matrix")
    printMatrix(L)
    print("U matrix")
    printMatrix(U)

