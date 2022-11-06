import functools

class Screen:
    _pixel_map = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

    def __init__(self, size_x, size_y):
        self.matrix = [["" for n in range(size_x)] for n in range(size_y)]

    def __str__(self):
        return functools \
        .reduce(lambda accum, row: accum + "".join(row) + "\n", self.matrix, "")
    
    def get_char(self, brightness): # value from 0 to 1.
        return self._pixel_map[round(min(brightness, 1) * (len(self._pixel_map)-1))]
