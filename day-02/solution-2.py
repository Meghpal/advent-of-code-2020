def solver():
    count = 0

    with open("input.txt") as f:
        for line in f:
            limits, letter, string = line.strip().split()
            letter = letter[:-1]
            ind_1, ind_2 = map(lambda elem: int(elem), limits.strip().split("-"))
            match = 0

            if string[ind_1 - 1] == letter:
                match += 1
            if string[ind_2 - 1] == letter:
                match += 1
            if match == 1:
                count += 1

    return count


print(solver())