import copy


def solver():
    li = []
    with open("input.txt") as f:
        for line in f:
            lii = list(line.strip())
            li.append(lii)

    xi = copy.deepcopy(li)
    for y in range(len(li)):
        for x in range(len(li[y])):
            if x > 0:
                if li[y][x] == "L" and li[y][x - 1] != "#":
                    xi[y][x] = "#"
    print(xi)


print(solver())