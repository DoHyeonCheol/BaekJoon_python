n = int(input())

for i in range(n) :
    print(str(" ") * int(n-i-1), str("*") * int(i+1), sep="")