from typing import List

class Solution:
    '''
    Input: nums = [2,3,-2,4]
    Output: 6
    Explanation: [2,3] has the largest product 6.
    '''
    def maxProduct(self, nums: List[int]) -> int:
        '''
        Runtime 137 ms
        Beats 70.30%
        '''
        minlist,maxlist = [nums[0]],[nums[0]]
        for i in range(1,len(nums)):
            minlist.append(min(nums[i], minlist[i-1]*nums[i], maxlist[i-1]*nums[i]))
            maxlist.append(max(nums[i], minlist[i-1]*nums[i], maxlist[i-1]*nums[i]))
        return max(maxlist)
    
    def maxProduct_dp(self, nums: List[int]) -> int:
        '''
        Runtime 233 ms
        Beats 12.55%
        '''
        def dp(i):
            if i==0 : return nums[i],nums[i]
            low,hi=dp(i-1)
            if nums[i]<0:
                low,hi=hi,low
            return min(low*nums[i],nums[i]),max(hi*nums[i],nums[i])
        
        return max(dp(i)[1] for i in range(len(nums)))
        
        
if __name__ == '__main__':
    answer=Solution().maxProduct_dp(
        #nums = [2,3,-2,4],
        #nums = [-2,0,-1],
        #nums = [-2,3,-4],
        #nums = [0,2],
        nums = [2,-5,-2,-4,3]
    )
    print(answer)