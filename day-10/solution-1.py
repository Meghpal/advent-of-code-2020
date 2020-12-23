def solver():
    li = []
    with open("input.txt") as f:
        for line in f:
            num = int(line.strip())
            li.append(num)

    li.sort()
    diff1 = 0
    diff3 = 1
    for i in range(len(li)):
        if i == 0:
            if li[i] == 3:
                diff3 += 1
            elif li[i] == 1:
                diff1 += 1
        if i > 0 and i <= len(li):
            if li[i] - li[i - 1] == 3:
                diff3 += 1
            elif li[i] - li[i - 1] == 1:
                diff1 += 1
    return diff1 * diff3


print(solver())