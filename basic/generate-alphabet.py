def alphabet():
    # ord is built-in function in python for getting int value of the char
    number_a = ord('a')
    number_z = ord('z')

    # char is built-in function in python for getting string from given number
    return [chr(i) for i in xrange(number_a, number_z + 1)]

if __name__ == '__main__':
    print alphabet()
