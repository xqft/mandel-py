import math
from numba import njit

import raster as rr

SIZE_X = 400
SIZE_Y = 150

OFF_X = 0
OFF_Y = 0

MAX_ITER = 10000

@njit
def mandel_sequence(ca, cb):
    a, b = 0, 0
    while True:
        yield a, b
        # (a+bi)^2 = a^2 - b^2 + 2abi
        a = a**2 - b**2 + ca
        b = 2*a*b + cb

@njit
def render(scale, off):
    matrix = rr.init_screen(SIZE_X, SIZE_Y)
    for x0 in range(SIZE_X):
        for y0 in range(SIZE_Y // 2):
            x = (x0 / SIZE_X * 2 - 1) * scale + OFF_X
            y = (1 - y0 / SIZE_Y * 2) * scale - OFF_Y

            for n, (a, b) in enumerate(mandel_sequence(x, y)):
                if n == MAX_ITER or (a < -2 or a > 2 or b < -2 or b > 2):
                    matrix[y0][x0] = rr.get_char(math.sin(n))
                    matrix[SIZE_Y - y0 - 1][x0] = rr.get_char(math.sin(n))
                    break
    return matrix

s = 1
while True:
    rr.print_screen(render(1/s))
    s = 1/2
