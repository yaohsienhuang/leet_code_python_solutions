from typing import List, Set, Dict, Tuple, Optional

class Solution:
    '''
    Input: nums = [0,0,1,1,1,2,2,3,3,4]
    Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
    Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
    It does not matter what you leave beyond the returned k (hence they are underscores).
    '''
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        Runtime: 100 ms, faster than 85.84% of Python3 online submissions for Remove Duplicates from Sorted Array.
        '''
        left = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[left] = nums[i]
                left += 1
        return left
                

if __name__ == '__main__':
    answer=Solution().removeDuplicates(
        nums=[0,0,1,1,1,2,2,3,3,4],
    )
    print(answer)