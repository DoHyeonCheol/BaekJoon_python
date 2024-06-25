h, m = map(int, input().split())

0 <= h <= 23 and 0 <= m <= 59

if m >= 45 :
    print(h, m - 45)
elif m < 45 :
    if h != 0 :
        print(h - 1, m + 15)
    elif h == 0 :
        print(23 - h, m + 15)