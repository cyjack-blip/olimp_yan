#
# Окружности
#

import math

xa, ya, ra = map(int, input("Введите три числа через пробел - данные окружности а (xa, ya, ra): ").split())
xb, yb, rb = map(int, input("Введите три числа через пробел - данные окружности b (xb, yb, rb): ").split())

# xa, ya, ra = [-1, -1, 1]
# xb, yb, rb = [-1, -3, 1]

d = math.sqrt((xb-xa) ** 2 + (yb-ya) ** 2)

if (xa, ya, ra) == (xb, yb, rb):
    print("a=b")  # совпадают
else:
    if d > (ra + rb):
        print("a|b")  # не пересекаются
    if d == (ra + rb):
        print("a.b")  # сопрекасаются
    if d < (ra + rb):
        if d < ra - rb:
            print("a>b")  # b внутри a
        elif d + ra < rb:
            print("b>a")  # a внутри b
        else:
            print("a^b")  # пересекаются
