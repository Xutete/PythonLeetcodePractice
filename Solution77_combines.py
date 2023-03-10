
# 我的思路 loop 不出来 n=4，k=2 好理解，但是n=4, k=3就不好求了
def combine(n, k):
    value_range = []
    res = []

    i = 1
    while i <= n:
        value_range.append(i)
        i += 1

    for left in range(len(value_range)):

        right = left + (k - 1)
        while right <= len(value_range) - 1:
            temp = []
            temp = temp.append(value_range[left])
            temp = temp.append(value_range[right])
            res.append(temp)

    return res


# backtracking 结构
def combine2(n, k):
    def backtrack(first=1, curr=[]):
        #print(str(curr))
        # if the combination is done
        if len(curr) == k:
            output.append(curr[:])

            return # 这里应该加一个return

        for i in range(first, n + 1):
            # add i into the current combination
            curr.append(i)
            # use next integers to complete the combination
            backtrack(i + 1, curr)
            # backtrack
            curr.pop()

    output = []
    backtrack()
    return output


n = 4
k = 2
r = combine2(4, 2)
print(r)


"""

"""




