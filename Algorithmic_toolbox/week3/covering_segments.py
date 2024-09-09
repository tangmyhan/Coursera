from sys import stdin
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []

    # Sắp xếp các đoạn theo điểm kết thúc của chúng
    segments.sort(key=lambda x: x.end)

    # Bắt đầu với điểm kết thúc của đoạn đầu tiên
    curr_point = segments[0].end
    points.append(curr_point)

    for s in segments:
        # Nếu điểm hiện tại không bao phủ được đoạn hiện tại
        if curr_point < s.start:
            curr_point = s.end
            points.append(curr_point)

    return points

if __name__ == '__main__':
    input = stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
