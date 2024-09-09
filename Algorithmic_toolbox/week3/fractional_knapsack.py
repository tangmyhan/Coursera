from sys import stdin


def optimal_value(capacity, weights, values):
    totalValue = 0.0
    # Tính toán tỷ lệ giá trị trên trọng lượng
    items = [(v / w, w, v) for w, v in zip(weights, values)]
    # Sắp xếp các vật phẩm theo tỷ lệ giá trị trên trọng lượng từ cao xuống thấp
    items.sort(key=lambda x: x[0], reverse=True)

    for i, weight, value in items:
        if capacity == 0:
            break
        # Lấy tối đa trọng lượng có thể từ vật phẩm hiện tại
        amount = min(weight, capacity)
        totalValue += i*amount
        capacity -= amount

    return totalValue


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
