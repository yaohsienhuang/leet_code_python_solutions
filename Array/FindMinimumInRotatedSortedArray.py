from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        Runtime 53 ms
        Beats 72.94%
        '''
        return min(nums)

    def findMin_binary(self, nums: List[int]) -> int:
        '''
        Runtime 42 ms
        Beats 91.36%
        '''
        low, high = 0, len(nums)-1
        min_value = nums[low]
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= nums[high]:  # right
                min_value = min(min_value, nums[high])
                low = mid + 1
            else:  # left
                min_value = min(min_value, nums[low], nums[mid])
                high = mid-1
        return min_value

    def findMin_binary2(self, nums: List[int]) -> int:
        '''
        Runtime 37 ms
        Beats 97.85%
        '''
        low, high = 0, len(nums)-1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] >= nums[high]:  # right
                low = mid + 1
            else:  # left
                high = mid

        return nums[low]


if __name__ == '__main__':
    answer = Solution().findMin_binary2(
        # nums = [3,4,5,1,2]
        # nums=[11,13,15,17]
        # nums=[3, 1, 2]
        nums=[2, 1]
    )
    print(answer)
