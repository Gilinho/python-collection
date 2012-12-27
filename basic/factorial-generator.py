def factorial(n):
    while (n > 0):
        yield n
        n -= 1
    print("Finish ...")

if __name__ == "__main__":
    number = 1
    for x in factorial(10):
        print(x)
        number = number * x
    print("Total: " + str(number))
