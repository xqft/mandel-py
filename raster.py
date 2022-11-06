import functools

from numba import njit

@njit
def init_screen(size_x, size_y):
    return [["" for n in range(size_x)] for n in range(size_y)]

@njit
def get_char(brightness): # value from 0 to 1.
    pixel_map = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
    return pixel_map[round(min(brightness, 1) * (len(pixel_map)-1))]

def print_screen(matrix):
    print(functools.reduce(lambda accum, row: accum + "".join(row) + "\n", matrix, ""))
