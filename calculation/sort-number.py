a = [1, 2, 3, 4, 5, 6, 1, 10, 12]

top = 0

def get_max(i):
    global top
    if int(i) > top:
        top = i

    return top

for c in a:
    get_max(c)

print top
