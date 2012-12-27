def fizzbuzz(i):
    while i > 0:
        val = i
        if (i % (3*5) == 0):
            val = "Fizz Buzz"
        elif(i % 3 == 0):
            val = "Fizz"
        elif(i % 5 == 0):
            val = "Buzz"
        yield val
        i -= 1

if __name__ == "__main__":
    for i in fizzbuzz(100):
        print i
