import numpy as np
from fractions import Fraction

if __name__ == "__main__":
    row = int(input("행을 입력해주세요: "))
    col = int(input("열을 입력해주세요: "))
    entries = list(map(int, input("component를 일렬로 space로 구별하여 입력해주세요(정수만): ").split()))
    # 수업에서 다룬 matrix 들
    # 0 6 -3 6 15 -5 -1 -2 6
    # 1 -3 -2 0 1 -2 1 -1 2 -4 3 2
    matrix = np.array(entries, dtype=Fraction).reshape(row, col)

    print(matrix)

    P = np.identity(row, dtype=Fraction)

    for r in range(row):
        if matrix[r][0] != 0:
            if r != 0:
                matrix[[r,0]] = matrix[[0,r]]
                P[[r,0]] = P[[0,r]]
                print("matrix의 첫번째 component가 0이 아니므로 partial pivoting PA=LU 사용")
                print(matrix)
            break
        if r == row-1:
            print("LU factorization 이 불가능합니다.")
            exit(1)
    # 분수가 나올 수 있으므로 type 을 Fraction 으로
    # Doolittle algorithm 사용
    U = np.zeros((row, col), dtype=Fraction)
    L = np.identity(row, dtype=Fraction )
    I = np.identity(row,dtype=Fraction)
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
    # 결과 출력 PA=LU 또는 A = LU 형태로 결과 출력
    if not np.all(np.equal(P, I)):
        print("PA = LU")
    else:
        print("A = LU")
    for r in range(row):
        if not np.all(np.equal(P,I)):
            for c in P[r]:
                print("%-6s"%str(c), end=" ")
            print(end="\t")
        for c in matrix[r]:
            print("%-6s" % str(c), end=" ")
        print(end="\t")
        if r == row//2:
            print("=",end="\t")
        else:
            print(end="\t")
        for c in L[r]:
            print("%-6s" % str(c), end=" ")
        print(end="\t")
        for c in U[r]:
            print("%-6s" % str(c), end=" ")
        print()


