class Solution:
    def reverseString(self, s):

        lower = 0
        higher = len(s) - 1

        if len(s) == 1:
            return s


        else:
            while lower < higher:
                temp = s[higher]
                s[higher] = s[lower]
                s[lower] = temp
                lower += 1
                higher -= 1

            return s



if __name__ == '__main__':
    x = Solution()

    #s = ['h', 'e', 'l', 'l', 'o']
    s = ['H', 'a', 'n', 'n', 'a', 'h']

    result = x.reverseString(s)
    print(result)

