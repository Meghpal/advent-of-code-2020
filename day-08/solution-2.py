def solver():
    li = []
    with open("input.txt") as f:
        for line in f:
            li.append(line.strip())

    j = 0
    while j < len(li):
        i = 0
        acc = 0
        vis = []
        looped = False

        li_changed = li.copy()

        op1, num1 = li_changed[j].split()
        if op1 == "jmp":
            li_changed[j] = "nop " + num1
            j += 1
        elif op1 == "nop":
            li_changed[j] = "jmp " + num1
            j += 1
        else:
            j += 1
            continue

        while i < len(li_changed):
            if i in vis:
                looped = True
                break
            else:
                vis.append(i)
            op, num = li_changed[i].split()
            num = int(num)
            if op == "acc":
                acc += num
                i += 1
            elif op == "jmp":
                i += num
            else:
                i += 1
        if looped == False:
            return acc


print(solver())