def fibonacci(n):
    if n <= 1:
        return n
    pre, curr = 0, 1
    for _ in range(n-1):
        pre, curr = curr, pre + curr
    return curr

n = int(input())
print(fibonacci(n))