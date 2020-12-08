from functools import reduce


def solver():
    trials = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    counts = [0 for x in trials]

    for j in range(len(trials)):
        i = 0
        with open("input.txt") as f:
            for line in f:
                line_clean = line.strip()
                if (
                    i % trials[j][1] == 0
                    and line_clean[
                        (trials[j][0] * int(i / trials[j][1])) % len(line_clean)
                    ]
                    == "#"
                ):
                    counts[j] += 1
                i += 1
    return reduce(lambda x, y: x * y, counts)


print(solver())