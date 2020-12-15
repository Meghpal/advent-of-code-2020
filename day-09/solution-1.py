from collections import deque


def solver():
    li = deque()
    pr_len = 25
    with open("input.txt") as f:
        for line in f:
            num = int(line.strip())
            curr_len = len(li)
            valid = True
            if curr_len == pr_len:
                valid = False
                for i in range(curr_len):
                    for j in range(i + 1, curr_len):
                        if li[i] + li[j] == num:
                            valid = True
                            break
                    if valid:
                        break
                li.popleft()
            if not valid:
                return num
            li.append(num)


print(solver())