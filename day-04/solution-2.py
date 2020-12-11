def solver():
    count = 0

    with open("input.txt") as f:
        for data in f.read().split("\n\n"):
            temp = data.replace("\n", " ").split(" ")
            c = 0
            for x in temp:
                if validate(x) == 1:
                    c += 1
            if c == 7:
                count += 1
    return count


def validate(x):
    a, b = x.split(":")
    if a == "byr":
        return 1 if int(b) >= 1920 and int(b) <= 2002 else 0
    elif a == "iyr":
        return 1 if int(b) >= 2010 and int(b) <= 2020 else 0
    elif a == "eyr":
        return 1 if int(b) >= 2020 and int(b) <= 2030 else 0
    elif a == "hgt":
        if b[-2] == "c":
            return 1 if int(b[:-2]) >= 150 and int(b[:-2]) <= 193 else 0
        elif b[-2] == "i":
            return 1 if int(b[:-2]) >= 59 and int(b[:-2]) <= 76 else 0
        else:
            return 0
    elif a == "hcl":
        if b[0] != "#" or len(b) != 7:
            return 0
        try:
            int(b[1:], 16)
        except:
            return 0
        else:
            return 1
    elif a == "ecl":
        return 1 if b in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"] else 0
    elif a == "pid":
        if len(b) == 9:
            try:
                int(b)
            except:
                return 0
            else:
                return 1
        else:
            return 0
    else:
        return 0


print(solver())