A = [[0]*100 for _ in range(100)]

n = int(input().rstrip())

for _ in range(n):
    a,b = map(int, input().split())

    for i in range(a, a+10):
        for j in range(b,b+10):
            A[i][j] = 1

Cnt = 0
for i in range(100):
    for j in range(100):
        if A[i][j] == 1:
            Cnt += 1

print(Cnt)