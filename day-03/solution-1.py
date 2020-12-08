def solver():
    count = 0

    with open("input.txt") as f:
        i = 0
        for line in f:
            line_clean = line.strip()

            if line_clean[(3 * i) % len(line_clean)] == "#":
                count += 1
            i += 1

    return count


print(solver())