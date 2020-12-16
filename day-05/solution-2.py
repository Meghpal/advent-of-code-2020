def solver():
    with open("input.txt") as f:
        l = []
        for line in f:
            clean_line = line.strip()
            row = int(
                "".join(map(lambda x: str(0) if x == "F" else str(1), clean_line[:7])),
                2,
            )
            col = int(
                "".join(map(lambda x: str(0) if x == "L" else str(1), clean_line[7:])),
                2,
            )
            l.append(row * 8 + col)
    l.sort()
    for i in range(len(l)):
        if i > 1 and l[i + 1] - l[i - 1] != 2:
            return i + l[1]


print(solver())