class Solution:
    def searchMatrix(self, matrix, target):
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS -1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                bot = row + 1
            elif target < matrix[row][0]:
                top = row - 1

            # actually, the value is in the current row
            # 所以这里我们找到了 具体在哪个row， 然后我们继续找 cols
            else:
                break

        # 在全部扫一遍后 None of the row contain the target value
        # 因为如果target很大，top就会一直+1，直到比bot还大，这个时候就证明target不在matrix里。
        # 同理，如果target很小，bot一直-1，直到-1，比0小，这个时候target不在matrix里。
        if not (top <= bot):
            return False

        '''
        a = False
        
        if not a:
            print('a is false.')
        '''

        # run binary search on current row
        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l +  r) // 2
            if target > matrix [row][m]:
                l = m + 1

            elif target < matrix [row][m]:
                r = m - 1
            else:
                return True

        # while 走完都没有发现的话 return False
        return False















