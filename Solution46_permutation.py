def permute(nums):
    result = []

    if len(nums) == 1:
        return [nums[:]]

    for i in range (len(nums)):
        n = nums.pop(0)
        print("n -> " + str(n))
        perms = permute(nums)
        print("perms ->" + str(perms))

        for perm in perms:
            perm.append(n)

        result.extend(perms)
        nums.append(n)

    return result


nums = [1, 2, 3]
r = permute(nums)
print(r)







"""
python list extend 方法
aList = [123, 'xyz', 'zara', 'abc', 123];
bList = [2009, 'manni'];
aList.extend(bList)

Extended List :  [123, 'xyz', 'zara', 'abc', 123, 2009, 'manni']

"""