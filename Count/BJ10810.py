import sys

N, M = map(int, sys.stdin.readline().split())

A = []

for n in range (N):
    A.append(0)

for m in range(M):
    i, j, k = map(int, sys.stdin.readline().split())
    for num in range(i-1, j):
        A[num] = k

for n in range(N):
    print(str(A[n]) + " ", end= '')