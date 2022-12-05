from typing import List

class Solution:
    '''
    Input: nums = [-1,1,0,-3,3]
    Output: [0,0,9,0,0]
    '''
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        Time Limit Exceeded
        '''
        length=len(nums)
        answer=[1]*length
        for i in range(len(nums)):
            except_self=nums[0:i]+nums[i+1:length]
            product=1
            for x in except_self:
                product*=x
            answer[i]=product
        return answer
    
    def productExceptSelf_2(self, nums: List[int]) -> List[int]:
        '''
        Runtime: 253 ms, faster than 85.84% of Python3 online submissions for Product of Array Except Self.
        '''
        #left to right
        answer=[1]
        for i in range(1,len(nums)): 
            answer.append(nums[i-1]*answer[i-1])
        # right to left
        right=1
        for i in range(len(nums)-1,-1,-1):
            right=right*nums[i+1] if len(nums)>i+1 else right
            answer[i]=answer[i]*right
        return answer        
        
if __name__ == '__main__':
    answer=Solution().productExceptSelf_2(
        #nums = [1,2,3,4],
        nums = [-1,1,0,-3,3],
    )
    print(answer)