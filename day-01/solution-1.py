def solver():
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

    for i in range(len(inp)):
        for j in range(i + 1, len(inp)):
            if inp[i] + inp[j] == 2020:
                return inp[i] * inp[j]


print(solver())