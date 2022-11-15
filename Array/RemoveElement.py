from typing import List

class Solution:
    '''
    Input: nums = [0,1,2,2,3,0,4,2], val = 2
    Output: 5, nums = [0,1,4,0,3,_,_,_]
    Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
    Note that the five elements can be returned in any order.
    It does not matter what you leave beyond the returned k (hence they are underscores).
    '''
    def removeElement(self, nums: List[int], val: int) -> int:
        '''
        Runtime: 72 ms, faster than 20.61% of Python3 online submissions for Remove Element.
        '''
        while val in nums:
            nums.remove(val)
        return len(nums)

    def removeElement2(self, nums: List[int], val: int) -> int:
        '''
        Runtime: 65 ms, faster than 46.37% of Python3 online submissions for Remove Element.
        '''
        k=0
        for i in range(len(nums)):
            if nums[i]==val:
                continue
            nums[k]=nums[i]
            k+=1
        return k

    def removeElement3(self, nums: List[int], val: int) -> int:
        '''
        Runtime: 33 ms, faster than 95.80% of Python3 online submissions for Remove Element.
        '''
        i = 0
        for x in nums:
            if x != val:
                nums[i] = x
                i += 1
        return i


if __name__ == '__main__':
    answer=Solution().removeElement(
        nums = [0,1,2,2,3,0,4,2],
        val = 2
    )
    print(answer)