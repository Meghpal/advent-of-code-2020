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

    return len(recurse("shiny gold bags", rel, set()))


def recurse(child, rel, sett):
    for elem in rel:
        for c in elem["c"]:
            if child[:-1] in c:
                sett.add(elem["p"])
                recurse(elem["p"], rel, sett)
                break
    return sett


print(solver())