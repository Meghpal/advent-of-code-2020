def solver():
    li = []
    with open("input.txt") as f:
        for line in f:
            num = int(line.strip())
            li.append(num)

    li.sort()
    arr = ""
    for i in range(len(li)):
        if i == 0:
            if li[i] == 3:
                arr += "3"
            elif li[i] == 1:
                arr += "1"
        elif i > 0 and i <= len(li):
            if li[i] - li[i - 1] == 3:
                arr += "3"
            elif li[i] - li[i - 1] == 1:
                arr += "1"
    arr += "3"
    print(arr)
    x = arr.split("3")
    print(x)
    poss = 1
    # for elem in x:
    #     if len(elem) != 0:
    #         poss *= 2 ** (len(elem) - 1)
    for i in range(len(x)):
        if len(x[i]) > 1:
            if i == 0 and len(x[i]) >= 3:
                poss *= 2 ** (len(x[i]) - 2)
            elif i == 0:
                poss *= 2 ** (len(x[i] - 1))
            else:
                poss *= 2 ** (len(x[i]) - 1)
    return poss


print(solver())