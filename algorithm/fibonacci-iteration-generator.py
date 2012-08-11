def fibo():
    a, b = 0, 1
    while 1:
        yield a
        a, b = b, a + b

if __name__ == '__main__':
    result = fibo()
    for i in range(100):
        print result.next()
