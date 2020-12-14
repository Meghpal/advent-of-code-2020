def solver():
    li = []
    with open("input.txt") as f:
        for line in f:
            li.append(line.strip())

    i = 0
    acc = 0
    vis = []
    while i < len(li):
        if i in vis:
            break
        else:
            vis.append(i)
        op, num = li[i].split()
        num = int(num)
        if op == "acc":
            acc += num
            i += 1
        elif op == "jmp":
            i += num
        else:
            i += 1
    return acc


print(solver())