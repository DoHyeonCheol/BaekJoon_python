n, t = map(int, input().split())

a = list(map(int, input().split()))

def isBiggerthant(x):
    return x < t

results = list(filter(isBiggerthant, a))

print(*results, sep=" ")