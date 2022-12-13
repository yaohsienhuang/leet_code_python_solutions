class Solution:
    def getSum(self, a: int, b: int) -> int:
        '''
        Runtime 35 ms
        Beats 85.88% 
        '''
        list=[a,b]
        return sum(list)
    
    
if __name__ == '__main__':
    answer=Solution().getSum(
        a=2,
        b=3,
    )
    print(answer)