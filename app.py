from raster.raster import Screen

SIZE_X = 400
SIZE_Y = 150

OFF_X = 1.5
OFF_Y = 0

MAX_ITER = 100

def mandel_sequence(ca, cb):
    a, b = 0, 0
    while True:
        yield a, b
        # (a+bi)^2 = a^2 - b^2 + 2abi
        a = a**2 - b**2 + ca
        b = 2*a*b + cb

screen = Screen(SIZE_X, SIZE_Y)

def render(scale):
    for x0 in range(SIZE_X):
        for y0 in range(SIZE_Y // 2):
            x = ((x0 - SIZE_X / 2) / SIZE_X * 2 - OFF_X / scale) * scale
            y = ((SIZE_Y / 2 - y0) / SIZE_Y * 2 - OFF_Y / scale) * scale

            for n, (a, b) in enumerate(mandel_sequence(x, y)):
                if n == MAX_ITER or (a < -2 or a > 2 or b < -2 or b > 2):
                    screen.matrix[y0][x0] = screen.get_char(n / MAX_ITER)
                    screen.matrix[SIZE_Y - y0 - 1][x0] = screen.get_char(n / MAX_ITER)
                    break
    print(screen)

s = 1
while True:
    render(1/s**2) 
    s += 1
