def fibonacci_sum_squares(to):
    if to <= 1:
        return to

    previous = 0
    current = 1
    tmp_previous = 0

    seq_sum = 1

    for i in range(2, 60):
        tmp_previous = current
        current = (previous + current) % 10
        previous = tmp_previous
        seq_sum = (seq_sum + current * current) % 10

    seq_sum = (seq_sum * ((to // 60) % 10)) % 10

    previous = 0
    current = 1
    tmp_previous = 0
    for i in range(60):
        if i <= 1 and i <= to % 60:
            seq_sum = (seq_sum + i) % 10
        elif i <= to % 60:
            tmp_previous = current
            current = (current + previous) % 10
            previous = tmp_previous
            seq_sum = (seq_sum + current * current) % 10

    return seq_sum

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    n = int(input().strip())
    print(fibonacci_sum_squares(n))
