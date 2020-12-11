def solver():
    count = 0

    with open("input.txt") as f:
        for data in f.read().split("\n\n"):
            count += len(set(data.replace("\n", "")))
    return count


print(solver())