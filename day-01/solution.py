def solver(puzzle_no=1):
    min_num = 3000
    inp = []

    with open("input.txt") as f:
        for line in f:
            num = int(line)
            if num < min_num:
                min_num = num
            inp.append(num)

    if min_num > 2020:
        return None

    if puzzle_no == 1:
        for i in range(len(inp)):
            for j in range(i + 1, len(inp)):
                if inp[i] + inp[j] == 2020:
                    return inp[i] * inp[j]
    else:
        for i in range(len(inp)):
            for j in range(i + 1, len(inp)):
                for k in range(j + 1, len(inp)):
                    if inp[i] + inp[j] + inp[k] == 2020:
                        return inp[i] * inp[j] * inp[k]


print(solver(1))
print(solver(2))
