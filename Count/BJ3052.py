number = list()

for i in range(10) :
    number.append(int(input())%42)

number = set(number)

print(len(number))

