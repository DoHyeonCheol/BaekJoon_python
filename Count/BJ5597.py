Student = [i for i in range (1, 31)]

for _ in range(28):
    Student.remove(int(input()))


for i in Student:
    print(i)