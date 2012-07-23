from timeit import Timer


def calculate(x, y):
    return x * y

if __name__ == '__main__':
    t = Timer("calculate(2, 34)", "from __main__ import  calculate")
    print t.timeit()
