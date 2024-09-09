n = int(input())
s = list(map(int, input().split()))

a = max(s)
s.remove(a)
b = max(s)
print(a*b)