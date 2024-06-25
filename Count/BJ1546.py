n = int(input())

score = [*map(int, input().split())]

m = max(score)
newscore=[]

for i in range(n) :
    newvalue=(score[i]/m)*100
    newscore.append(newvalue)

newavg=sum(newscore)/n

print(newavg)