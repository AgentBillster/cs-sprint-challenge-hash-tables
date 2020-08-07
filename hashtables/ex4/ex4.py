def has_negatives(a):
    """
    YOUR CODE HERE
    """
    d = {}
    arr = []

    for i in a:
        if i > 0:
            if i not in d:
                d[i] = 0
            else:
                d[i] += 1
        if i < 0:
            x = i * -1
            if x in d:
                d[x] += 1
            else:
                d[x] = 0

    for i in d.items():
        if i[1] == 1:
            arr.append(i[0])

    print(d)

    return arr


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
