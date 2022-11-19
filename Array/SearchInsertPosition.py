from typing import List

class Solution:
    '''
    Input: nums = [1,3,5,6], target = 5
    Output: 2
    '''
    def searchInsert(self, nums: List[int], target: int) -> int:
        '''
        Runtime: 134 ms, faster than 5.33% of Python3 online submissions for Search Insert Position.
        '''
        for i, num in enumerate(nums):
            if num == target:
                return i
            if num >= target:
                return i
        return len(nums)

    def searchInsert_binarySearch(self, nums: List[int], target: int) -> int:
        '''
        Runtime: 113 ms, faster than 27.22% of Python3 online submissions for Search Insert Position.
        '''
        low, high = 0, len(nums)
        while low < high:
            mid = (low + high) // 2
            if target > nums[mid]:
                low = mid + 1
            else:
                high = mid
        return low

if __name__ == '__main__':
    answer=Solution().searchInsert_binarySearch(
        #nums = [1,3,5,6], target = 7
        nums = [1,3,5,6], target = 5
    )
    print(answer)