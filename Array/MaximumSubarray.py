from typing import List

class Solution:
    '''
    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6.
    '''
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        Runtime 877 ms, Beats 79.90%
        '''
        total_sum = nums[0]
        max_sum = nums[0]
        for i in range(len(nums)):
            total_sum = max(total_sum + nums[i], nums[i])
            max_sum = max(total_sum, max_sum)
        return max_sum
        
        
if __name__ == '__main__':
    answer=Solution().maxSubArray(
        #nums = [1,2,3,4],
        nums = [-2,1,-3,4,-1,2,1,-5,4],
    )
    print(answer)