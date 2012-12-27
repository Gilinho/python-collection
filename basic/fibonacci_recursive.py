def fib():
    a, b = 0, 1

    while 1:
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    a = fib()
    for x in range(20):
        print a.next()