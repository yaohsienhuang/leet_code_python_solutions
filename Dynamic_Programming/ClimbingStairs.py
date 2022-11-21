

class Solution:
    '''
    Input: n = 3
    Output: 3
    Explanation: There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step
    '''
    def climbStairs(self, n: int) -> int:
        '''
        n=1:1
        n=2:2
        n=3:3
        n=4:5 -> 2+3
        n=5:8 -> 3+5
        Runtime: 36 ms, faster than 85.85% of Python3 online submissions for Climbing Stairs.
        '''
        prev, current = 0, 1
        for i in range(n):
            prev, current = current, prev + current
        return current

if __name__ == '__main__':
    answer=Solution().climbStairs(
        n = 5
    )
    print(answer)