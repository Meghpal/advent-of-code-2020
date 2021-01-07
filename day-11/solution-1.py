import copy


def safe_checker(li, x, y, val):
    # with great power comes great responsibility
    if x < 0 or y < 0:
        return False
    try:
        return li[y][x] == val
    except:
        return False


def solver():
    li = []
    with open("input.txt") as f:
        for line in f:
            lii = list(line.strip())
            li.append(lii)

    xi = copy.deepcopy(li)
    while True:
        updates = 0
        for y in range(len(li)):
            for x in range(len(li[y])):

                occupied = 0
                occupied += 1 if (safe_checker(li, x - 1, y, "#")) else 0
                occupied += 1 if (safe_checker(li, x + 1, y, "#")) else 0
                occupied += 1 if (safe_checker(li, x, y - 1, "#")) else 0
                occupied += 1 if (safe_checker(li, x, y + 1, "#")) else 0
                occupied += 1 if (safe_checker(li, x - 1, y - 1, "#")) else 0
                occupied += 1 if (safe_checker(li, x + 1, y - 1, "#")) else 0
                occupied += 1 if (safe_checker(li, x - 1, y + 1, "#")) else 0
                occupied += 1 if (safe_checker(li, x + 1, y + 1, "#")) else 0

                if li[y][x] == "L" and occupied == 0:
                    xi[y][x] = "#"
                    updates += 1
                elif li[y][x] == "#" and occupied > 3:
                    xi[y][x] = "L"
                    updates += 1

        if updates != 0:
            li = copy.deepcopy(xi)
        else:
            break

    count = 0
    for y in range(len(xi)):
        for x in range(len(xi[y])):
            count += 1 if safe_checker(xi, x, y, "#") else 0
    return count


print(solver())