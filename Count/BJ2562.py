n=9
list=[]

for i in range(n):
    list.append(int(input()))
    
print(max(list))
print(list.index(max(list))+1)