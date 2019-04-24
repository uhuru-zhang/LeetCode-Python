import math
import random
import time
from decimal import Decimal


def get_triangle_area(triangle: [[float]]) -> float:
    a = get_length((triangle[0], triangle[1]))
    b = get_length((triangle[0], triangle[2]))
    c = get_length((triangle[1], triangle[2]))

    p = (a + b + c) / Decimal(2)
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


def get_length(line: [[float]]) -> Decimal:
    line = [[Decimal(x), Decimal(y)] for x, y in line]
    return ((line[1][1] - line[0][1]) ** Decimal(2) + (line[1][0] - line[0][0]) ** Decimal(2)).sqrt()


def in_a_line(point: [float], line: [[float]]) -> bool:
    return get_triangle_area((point, line[0], line[1])) == Decimal(0)


def in_middle_of_a_line(point: [float], line: [[float]]) -> bool:
    if in_a_line(point, line):
        return get_length(line) == get_length((point, line[0])) + get_length((point, line[1]))
    return False


def in_triangle(point: [float], triangle: [[float]]) -> bool:
    if in_middle_of_a_line(point, (triangle[0], triangle[1])) or \
            in_middle_of_a_line(point, (triangle[0], triangle[2])) or \
            in_middle_of_a_line(point, (triangle[1], triangle[2])):
        return True

    area = get_triangle_area(triangle)

    area_1 = get_triangle_area((point, triangle[0], triangle[1]))
    area_2 = get_triangle_area((point, triangle[0], triangle[2]))
    area_3 = get_triangle_area((point, triangle[1], triangle[2]))

    return area - sum([area_1, area_2, area_3]) == 0


def below_line(point, line):
    line = [[Decimal(x), Decimal(y)] for x, y in line]
    point = [Decimal(point[0]), Decimal(point[1])]

    k = (line[1][1] - line[0][1]) / (line[1][0] - line[0][0])
    b = line[0][1] - k * line[0][0]

    y = k * point[0] + b
    return point[1] < y


def brute_force_convex_hull(points: [[float]]) -> [[float]]:
    flags = [True for _ in range(len(points))]
    last_length_of_flags = sum(flags)

    while True:
        for i_0 in range(len(points)):
            if not flags[i_0]:
                continue
            for i_1 in range(len(points)):
                if not flags[i_1] or i_1 == i_0:
                    continue
                for i_2 in range(len(points)):
                    if not flags[i_2] or i_2 in (i_0, i_1):
                        continue
                    for i_3 in range(len(points)):
                        if not flags[i_3] or i_3 in (i_0, i_1, i_2):
                            continue

                        if in_triangle(points[i_0], (points[i_1], points[i_2], points[i_3])):
                            flags[i_0] = False

        if last_length_of_flags == sum(flags):
            break

        last_length_of_flags = sum(flags)

    result_points = [point for i, point in enumerate(points) if flags[i]]
    result_points = sorted(result_points, key=lambda a: a[0])

    result = []
    blow_up = []
    max_index = 1
    result.append(result_points[0])
    result_points.pop(0)
    result.append(result_points[-1])
    result_points.pop(-1)

    for point in result_points:
        blow_up.append(below_line(point, (result[0], result[max_index])))
        if below_line(point, (result[0], result[max_index])):
            result.insert(max_index, point)
            max_index += 1
        else:
            result.insert(max_index + 1, point)
    return result





if __name__ == '__main__':
    random.seed()

    for i in range(1, 11):
        n = i * 1000
        points = []
        for _ in range(n):
            points.append((random.random() * 100, random.random() * 100))
        begin = time.time()
        brute_force_convex_hull(points)
        end = time.time()

        print("graham_scan, n: {}, time: {}".format(n, end - begin))

    # points = [
    #     (207, 184), (393, 60), (197, 158), (197, 114), (128, 261), (442, 40),
    #     (237, 159), (338, 75), (194, 93), (33, 159), (393, 152), (433, 267),
    #     (324, 141), (384, 183), (273, 165), (250, 257), (423, 198), (227, 68),
    #     (120, 184), (214, 49), (256, 75), (379, 93), (312, 49), (471, 187),
    #     (366, 122)
    # ]
    # result = brute_force_convex_hull(points)
    # [(33, 159), (214, 49), (442, 40), (471, 187), (433, 267), (128, 261)]
    # [(33, 159), (214, 49), (442, 40), (471, 187), (433, 267), (128, 261)]
    #
    # print(result)