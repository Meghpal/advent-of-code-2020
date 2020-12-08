from collections import Counter


def solver():
    count = 0

    with open("input.txt") as f:
        for line in f:
            limits, letter, string = line.strip().split()
            letter = letter[:-1]
            min_num, max_num = map(lambda elem: int(elem), limits.strip().split("-"))
            repetitions = Counter(string)[letter]

            if repetitions >= min_num and repetitions <= max_num:
                count += 1

    return count


print(solver())