def fibonacci_last_digit(n):
    if n <= 1:
        return n
    pre, curr = 0, 1
    for _ in range(n-1):
        pre, curr = curr%10, (pre + curr)%10
    return curr%10

n = int(input())
print(fibonacci_last_digit(n))