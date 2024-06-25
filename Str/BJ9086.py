n= int(input())

for i in range(n):
    sen = [*map(str, input())]
    print(sen[0]+sen[-1])