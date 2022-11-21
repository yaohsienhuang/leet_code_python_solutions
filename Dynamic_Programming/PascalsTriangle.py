from typing import List

class Solution:
    '''
    Input: numRows = 5
    Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
    '''
    def generate(self, numRows: int) -> List[List[int]]:
        '''
        Runtime: 65 ms, faster than 19.64% of Python3 online submissions for Pascal's Triangle.
        '''
        triangle=[[1],[1,1]]
        if numRows==1:
            return [triangle[0]]
        for i in range(3,numRows+1):
            last=triangle[-1]
            center=[]
            for j in range(len(last)-1):
                center.append(last[j]+last[j+1])
            triangle.append([1]+center+[1])
        return triangle
    
    def generate2(self, numRows: int) -> List[List[int]]:
        '''
        Runtime: 45 ms, faster than 75.24% of Python3 online submissions for Pascal's Triangle.
        '''
        triangle = []
        for i in range(numRows):
            triangle.append([1])
            if i > 1: 
                for j in range(i-1):
                    triangle[i].append(triangle[i-1][j]+triangle[i-1][j+1])
            if i > 0:
                triangle[i].append(1)
        return triangle

if __name__ == '__main__':
    answer=Solution().generate2(
        numRows = 2
    )
    print(answer)