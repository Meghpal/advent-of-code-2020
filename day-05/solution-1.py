def solver():
    mx = 0

    with open("input.txt") as f:
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
            mx = max(row * 8 + col, mx)
    return mx


print(solver())