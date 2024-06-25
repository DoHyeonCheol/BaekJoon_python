n = int(input())

for _ in range(n):
    a, word = input().split()
    for i in word :
        print(i*int(a), end='')
    print()