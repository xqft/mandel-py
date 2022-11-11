from numba import njit

import raster as rr

@njit
def mandel_sequence(ca, cb):
    a, b = 0, 0
    while True:
        yield a, b
        a, b = a**2 - b**2 + ca, 2*a*b + cb
        # (a+bi)^2 = a^2 - b^2 + 2abi

@njit
def screen_to_complex(x0, y0, off_x, off_y, size_x, size_y, scale):
    return ((x0 / size_x * 2 - 1) * scale + off_x, 
            (1 - y0 / size_y * 2) * scale - off_y)

@njit
def gen_mandel_matrix(max_iter, size_x, size_y, scale, off_x, off_y):
    matrix = rr.init_screen(size_x, size_y)
    for x0 in range(size_x):
        for y0 in range(size_y):
            x, y = screen_to_complex(x0, y0, off_x, off_y, size_x, size_y, scale)

            for n, (a, b) in enumerate(mandel_sequence(x, y)):
                if n == max_iter or (a < -2 or a > 2 or b < -2 or b > 2):
                    matrix[y0][x0] = rr.get_char(n / max_iter)
                    break
    return matrix

# Initially all the previous variables were going to be properties of a Screen class, but
# I couldn't make numba's compiler work with it.
