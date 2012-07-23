# Insertion Sort Algorithm
# ---------------------------
# Just imagine when you playing cards and start to sorting by it value.
# [ Q, 2, K, As, 5, 4 ] and you will ordering it from right <--> left

def insert_sort(number):
    for i, j in enumerate(number):
        current = number[i]
        prev = i - 1

        while prev >= 0 and number[prev] > current:
            number[prev+1] = number[prev]
            prev -= 1
        number[prev+1] = current
    return number

if __name__ == '__main__':
    number = [11, 27, 89, 3, 6, 8, 9, 10, 1]
    print number
    print insert_sort(number)


