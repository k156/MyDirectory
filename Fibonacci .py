
def func():
    x = 0
    y = 1
    while x < 101:
        n = x + y
        print(x, y, n)
        x = y + n
        y = x + n
        # return x, y, n

func()