def change(m):
    return (m//10) + ((m%10)//5) + (m%10)%5

m = int(input())
print(change(m))
    