def mul(j, m, b):
    b.append(j * m)


def run():
    a = [3, 2, 7, 9, 6]
    b = []
    for i in a:
        if i % 3 == 0:
            continue
        elif i % 2 == 0:
            mul(i, 5, b)
        else:
            mul(i, 2, b)
    print(b)


run()

