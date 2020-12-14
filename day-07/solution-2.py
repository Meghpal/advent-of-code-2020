def solver():
    with open("input.txt") as f:
        rel = []

        for line in f:
            parent, children = line.strip().split("contain")
            parent = parent.strip()
            children = children[:-1].strip()
            temp = {"p": parent}
            temp["c"] = children.split(", ")
            rel.append(temp)

    return recurse("1 shiny gold bag", rel) - 1


def recurse(parent, rel):
    for elem in rel:
        if parent[2:-1] in elem["p"]:
            temp = 0
            for c in elem["c"]:
                if c == "no other bags":
                    return 1
                z = recurse(c, rel)
                if z == 1:
                    temp += int(c[0]) * z
                else:
                    temp += z
            return int(parent[0]) + int(parent[0]) * temp


print(solver())