import heapq


class Solution31_NextPermutation_bruteforce:
    def nextPermutation(self, nums):

        '''
        Time : O (N!)
        Space: O (N)
        '''
        def backtrack(first = 0):
            '''
            Permutation-generating recursive function
            '''

            if first == len(nums):
                permutations.append(nums[:])


            for i in range(first, len(nums)):
                # 快捷写法
                nums[first], nums[i] = nums[i], nums[first]

                backtrack(first + 1)

                # 快捷写法
                nums[first], nums[i] = nums[i], nums[first]

        # Generate all permutations from 'nums'
        permutations = []
        backtrack()

        # Build a Min-Heap based on permutation already generated
        heapq.heapify(permutations)

        # In case 'nums' is the last permutation, return first permutation
        if nums == permutations[-1]:
            return permutations[0]

        # Otherwise finds and returns next permutation
        while heapq:
            permutation = heapq.heappop(permutations)
            if nums == permutation:
                next_permutation = heapq.heappop(permutations)
                return next_permutation














