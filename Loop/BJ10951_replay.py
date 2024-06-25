# try except 자세히 공부한번하기

import sys

while True:
    try :
        a, b = map(int, sys.stdin.readline().split())
    
    except :
        break

    print(a+b)

    