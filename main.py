import sys

t = int(input())
n = int(input())

ar = []
for i in range(n):
    ar.append(int(input()))

ar.sort()
total = 0
for i in range(n):
    if total+ar[i] > t:
        print(i)
        sys.exit()
    total += ar[i]


