import math


def square(side_length, method='round'):
    area = side_length * side_length
    if method == 'ceil':
        return math.ceil(area)
    elif method == 'floor':
        return math.floor(area)
    else:
        return round(area)


side = 4  # длина стороны
print(f"Общая площадь без округления: {side * side}")
print(f"Площадь с округлением round: {square(side, 'round')}")
print(f"Площадь с округлением ceil: {square(side, 'ceil')}")
print(f"Площадь с округлением floor: {square(side, 'floor')}")
