import math
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

    return area - sum([area_1, area_2, area_3]) == Decimal(0)


def get_cos(triangle: [[float]]) -> Decimal:
    a = get_length((triangle[1], triangle[2]))
    b = get_length((triangle[0], triangle[1]))
    c = get_length((triangle[0], triangle[2]))

    return (b ** Decimal(2) + c ** Decimal(2) - a ** Decimal(2)) / (Decimal(2) * b * c)


def graham_scan(points: [[float]]) -> [[float]]:
    # min_y = min(points, key=lambda point: float(str(point[1]) + "." + str(point[0])))
    min_y = points[0]
    for point in points:
        if point[1] < min_y[1]:
            min_y = point
        elif point[1] == min_y[1]:
            if min_y[0] < point[0]:
                min_y = point

    max_x = max(points, key=lambda point: point[0])
    points.remove(min_y)

    points = sorted(points, key=lambda point: math.acos(get_cos((min_y, point, (max_x[0] + 1, min_y[1])))))

    result = [min_y, points[0]]
    points.pop(0)

    for point in points:
        if math.fabs(get_cos((min_y, point, (max_x[0] + 1, min_y[1]))) - get_cos(
                (min_y, result[-1], (max_x[0] + 1, min_y[1])))) <= 0.1 ** 32:
            result[-1] = max((result[-1], point), key=lambda point: get_length((min_y, point)))
        else:
            result.append(point)

            while len(result) > 3 and in_triangle(result[-2], [min_y, result[-1], result[-3]]):
                result.pop(-2)

    return result


def divide_and_conquer(points: list) -> list:
    if len(points) <= 3:
        result = graham_scan(points)

        min_x_index = 0
        for i in range(1, len(result)):
            if result[min_x_index][0] > result[i][0]:
                min_x_index = i
            elif result[min_x_index][0] == result[i][0]:
                if result[min_x_index][1] > result[i][1]:
                    min_x_index = i

        return result[min_x_index:] + result[:min_x_index]

    left = divide_and_conquer(points[:len(points) // 2])
    right = divide_and_conquer(points[len(points) // 2:])

    a = left[1:]

    min_x = left[0]

    def get_polar_angle(point):
        return math.acos(get_cos([min_x, point, (min_x[0], min_x[1] - 1)]))

    max_right_index = min_right_index = 0
    for i in range(1, len(right)):
        if get_polar_angle(right[i]) > get_polar_angle(right[max_right_index]):
            max_right_index = i
        elif get_polar_angle(right[i]) == get_polar_angle(right[max_right_index]):
            if get_length((right[i], min_x)) > get_length((right[max_right_index], min_x)):
                max_right_index = i

        if get_polar_angle(right[i]) < get_polar_angle(right[min_right_index]):
            min_right_index = i
        elif get_polar_angle(right[i]) == get_polar_angle(right[min_right_index]):
            if get_length((right[i], min_x)) < get_length((right[min_right_index], min_x)):
                min_right_index = i

    if max_right_index > min_right_index:
        b = right[min_right_index: max_right_index + 1]
        c = (right[max_right_index + 1:] + right[:min_right_index])[::-1]
    else:
        b = right[min_right_index:] + right[:max_right_index + 1]
        c = right[max_right_index: min_right_index + 1]

    tmp_points = []
    min_indexes = [0, 0, 0]
    abc = [a, b, c]

    while not (min_indexes[0] >= len(a) and min_indexes[1] >= len(b) and min_indexes[2] >= len(c)):
        min_i = -1
        for i in range(0, 3):
            if min_indexes[i] < len(abc[i]):
                if min_i == -1:
                    min_i = i
                else:
                    if get_polar_angle(abc[i][min_indexes[i]]) < get_polar_angle(abc[min_i][min_indexes[min_i]]):
                        min_i = i
        tmp_points.append(abc[min_i][min_indexes[min_i]])
        min_indexes[min_i] += 1

    result = [min_x]
    for point in tmp_points:
        result.append(point)

        while len(result) > 3 and in_triangle(result[-2], [min_x, result[-1], result[-3]]):
            result.pop(-2)

    return result


if __name__ == '__main__':
    # random.seed()
    #
    # for i in range(1, 11):
    #     n = i * 1000
    #     points = []
    #     for _ in range(n):
    #         points.append((random.random() * 100, random.random() * 100))
    #     begin = time.time()
    #     graham_scan(points)
    #     end = time.time()
    #
    #     print("graham_scan, n: {}, time: {}".format(n, end - begin))
    #
    #     points = []
    #     for _ in range(n):
    #         points.append((random.random() * 100, random.random() * 100))
    #     points = sorted(points, key=lambda point: point[0])
    #
    #     begin = time.time()
    #     divide_and_conquer(points)
    #     end = time.time()
    #     print("divide_and_conquer, n: {}, time: {}".format(n, end - begin))


    points = [
        (207, 184), (393, 60), (197, 158), (197, 114), (128, 261), (442, 40),
        (237, 159), (338, 75), (194, 93), (33, 159), (393, 152), (433, 267),
        (324, 141), (384, 183), (273, 165), (250, 257), (423, 198), (227, 68),
        (120, 184), (214, 49), (256, 75), (379, 93), (312, 49), (471, 187),
        (366, 122)
    ]
    print(graham_scan(points))

    points = [
        (207, 184), (393, 60), (197, 158), (197, 114), (128, 261), (442, 40),
        (237, 159), (338, 75), (194, 93), (33, 159), (393, 152), (433, 267),
        (324, 141), (384, 183), (273, 165), (250, 257), (423, 198), (227, 68),
        (120, 184), (214, 49), (256, 75), (379, 93), (312, 49), (471, 187),
        (366, 122)
    ]
    points = sorted(points, key=lambda point: point[0])
    print(divide_and_conquer(points))

    [(442, 40), (471, 187), (433, 267), (128, 261), (33, 159), (214, 49)]
