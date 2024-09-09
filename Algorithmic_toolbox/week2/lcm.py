def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

def lcm(a,b):
    l = gcd(a,b)
    return int((a*b)/l)

a, b = map(int, input().split())
print(lcm(a,b))