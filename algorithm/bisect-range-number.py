from bisect import bisect


def grades(score, breakpoints=[60, 70, 80, 90], result='FDCBA'):
    grade = bisect(breakpoints, score)
    return result[grade]

if __name__ == '__main__':
    print grades(71)
