words = 'A A A B C B B C C C B C A'.split()
major = words[0]
total = 0

for w in words:
    if not major:
        major, total = w, 0
    elif major == w:
        total += 1
    elif major != w:
        total -= 1
        if total <= 0:
            total, major = 0, ''

    print total, major, w
