from typing import List

class Solution:
    '''
    Input: nums = [1,2,3,1]
    Output: true
    '''
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        Runtime: 454 ms, faster than 97.40% of Python3 online submissions for Contains Duplicate.
        '''
        counts={}
        Duplicate=False
        for num in nums:
            if num in counts:
                return True
            else:
                counts[num]=0
        return Duplicate
        
if __name__ == '__main__':
    answer=Solution().containsDuplicate(
        #nums = [1,1,1,3,3,4,3,2,4,2],
        nums = [1,2,3,4],
    )
    print(answer)