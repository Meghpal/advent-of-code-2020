def solver():
    count = 0

    with open("input.txt") as f:
        for data in f.read().split("\n\n"):
            temp = data.replace("\n", " ").split(" ")
            if len(temp) >= 8:
                count += 1
            elif len(temp) == 7:
                c = 0
                for x in temp:
                    if not (x.startswith("cid")):
                        c += 1
                if c == 7:
                    count += 1

    return count


print(solver())