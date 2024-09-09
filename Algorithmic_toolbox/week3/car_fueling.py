from sys import stdin

def min_refills(distance, tank, stops):
    # Thêm điểm bắt đầu (0) và điểm kết thúc (distance) vào danh sách stops
    stops = [0] + stops + [distance]
    curr_refill = 0
    num_refill = 0

    while (curr_refill < len(stops)-1):
        last_refill = curr_refill
        # Di chuyển đến trạm xăng xa nhất có thể từ vị trí hiện tại
        while ((curr_refill < len(stops)-1) and 
               (stops[curr_refill + 1] - stops[last_refill] <= tank)):
            curr_refill += 1
        
        # Nếu không thể di chuyển xa hơn, kiểm tra điều kiện kết thúc
        if curr_refill == last_refill:
            return -1
        
         # Nếu chưa đến đích, đổ xăng
        if curr_refill < len(stops)-1:
            num_refill += 1

    return num_refill


if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))
