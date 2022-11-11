from numba import njit

import raster as rr
import mandel as ml

import time

(OFF_X, OFF_Y) = (-0.34853774148008254, -0.6065922085831237)

def limit_fps(fps):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time.time()

            func(*args, **kwargs)

            end = time.time()
            if (end - start < 1/fps):
                time.sleep(1/fps - end + start)
        return wrapper
    return decorator

@limit_fps(10)
def loop(s):
    matrix = ml.gen_mandel_matrix(  max_iter = 1000,
                                    size_x = 400, size_y = 150,
                                    scale = 1/s**2,
                                    off_x = OFF_X, off_y = OFF_Y)
    rr.print_screen(matrix)

s = 1
while True:
    loop(s)
    s += 1
