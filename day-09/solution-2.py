def solver():
    li = []
    pr_len = 25
    start = 0
    with open("input.txt") as f:
        for line in f:
            num = int(line.strip())
            curr_len = len(li)
            valid = True
            if curr_len == pr_len + start:
                valid = False
                for i in range(start, curr_len - 1):
                    for j in range(i + 1, curr_len):
                        if li[i] + li[j] == num:
                            valid = True
                            break
                    if valid:
                        break
                start = start + 1
            if not valid:
                for i in range(curr_len - 1):
                    for j in range(i + 1, curr_len):
                        if sum(li[i:j]) == num:
                            return max(li[i:j]) + min(li[i:j])

            li.append(num)


print(solver())