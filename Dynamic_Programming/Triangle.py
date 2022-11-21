from typing import List

class Solution:
    '''
    Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    Output: 11
    Explanation: The triangle looks like:
           2
          3 4
         6 5 7
        4 1 8 3
    The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
    '''
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        '''
        wrong answer
        you may move to an adjacent number of the row below.
        '''
        sum=0
        for i in triangle:
            sum+=min(i)
        return sum

    def minimumTotal2(self, triangle: List[List[int]]) -> int:
        '''
        Runtime: 176 ms, faster than 17.43% of Python3 online submissions for Triangle.
        '''
        for i in range(len(triangle)):
            for j in range(len(triangle[i])):
                triangle[i][j] += (min(
                        triangle[i-1][j] if j<len(triangle[i-1]) else +float('inf'), 
                        triangle[i-1][j-1] if (j-1>=0) else +float('inf')) if (i - 1 >=0) else 0
                    )
        return min(triangle[-1])
    
    def minimumTotal3(self, triangle: List[List[int]]) -> int:
        '''
        Runtime: 81 ms, faster than 83.99% of Python3 online submissions for Triangle.
        '''
        for i in range(1,len(triangle)):
            for j in range(i+1):
                print(i,'-',j)
                temp1, temp2 = float('inf'), float('inf')
                if j-1>=0:
                    temp1 = triangle[i-1][j-1]
                if j<i:
                    temp2 = triangle[i-1][j]
                triangle[i][j] = min(temp1, temp2)+triangle[i][j]
        return min(triangle[-1])

if __name__ == '__main__':
    answer=Solution().minimumTotal3(
        #triangle = [[-1],[2,3],[1,-1,-3]]
        triangle = [[2],[3,4],[6,5,7],[4,1,8,3]],
        #triangle = [[-10]]
    )
    print(answer)