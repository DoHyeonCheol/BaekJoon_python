n = []
max = 0

for i in range(5):
    n.append(input())
    if max <= len(n[i]):
        max = len(n[i])

for i in range(max):
    for j in range(5):
        try :
            print(f'{n[j][i]}', end='')
        except IndexError:
            continue