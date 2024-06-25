a = int(input())
b = int(input())

s = 0

for i in range (1, b+1):
    x, y = map(int, input().split())
    s += x * y 


if a == s :
    print("Yes")
else :
    print("No")