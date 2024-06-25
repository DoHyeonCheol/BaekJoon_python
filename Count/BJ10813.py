import sys

N, M = map(int, sys.stdin.readline().split())

Basket = [(i+1) for i in range (N)]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    Basket[i-1], Basket[j-1] = Basket[j-1], Basket[i-1]
    
print(*Basket)