from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        Runtime 784 ms
        Beats 89.59%
        '''
        l, r = 0, len(height)-1
        area = 0
        while l < r:
            a = min(height[r], height[l]) * (r-l)
            area = max(a, area)
            if height[r] < height[l]:
                r -= 1
            else:
                l += 1
        return area
        
if __name__ == '__main__':
    answer=Solution().maxArea(
        height = [1,8,6,2,5,4,8,3,7],
    )
    print(answer)