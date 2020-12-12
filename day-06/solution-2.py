from collections import Counter


def solver():
    count = 0

    with open("input.txt") as f:
        for data in f.read().split("\n\n"):
            x = Counter(data)
            count += len(
                Counter({key: num for key, num in x.items() if num == x["\n"] + 1})
            )
    return count


print(solver())