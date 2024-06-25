x = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = input()
time = 0

for _ in range(len(word)) :  
    for i in x:  
        if word[_] in i :  
            time += x.index(i) +3  
print(time)