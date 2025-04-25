# pylint: skip-file
calculate_distance = lambda x1, x2: abs(x1 - x2)

calculate_segments = lambda length_a, length_b: length_a // length_b

calculate_digit_sum = lambda number: sum(int(d) for d in str(abs(number)))


def calculate_rect_area(x1, y1, x2, y2):
    width = abs(x1 - x2)
    height = abs(y1 - y2)
    return width * height

def round_to_multiple(number, multiple):
    return multiple * round(number / multiple)