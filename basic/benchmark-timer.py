from timeit import Timer

def calculate(x, y):
    return x * y

if __name__ == '__main__':
    t = Timer("calculate(100009, 1000000)", "from __main__ import  calculate")
    print t.timeit()
