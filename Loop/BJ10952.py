import sys

while True:
    x, y = map(int, sys.stdin.readline().split())
    
    if x != 0 or y !=0 :
        print(x + y)
    
    else :
        break