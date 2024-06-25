n, m = map(int, (input().split()))

A = []
B = []
C = []

for i in range(n):
    AA = list(map(int, input().split()))
    A.append(AA)

for i in range(n):
    BB = list(map(int, input().split()))
    B.append(BB)

for i in range(n):
    for j in range(m):
        C.append(A[i][j]+B[i][j])
    print(*C)

    C.clear()
