from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        Runtime 74 ms
        Beats 61.24%
        '''
        try :
            idx=nums.index(target)
        except:
            idx=-1
        return idx
    
    def search_binary(self, nums: List[int], target: int) -> int:
        
        '''
        Runtime 46 ms
        Beats 85.81%
        '''
        if not nums:
            return -1

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid
            if target == nums[high]:
                return high
            if target == nums[low]:
                return low

            if nums[low] <= nums[mid]: 
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:    # [5,1,2,3,4]
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1
            
if __name__ == '__main__':
    answer=Solution().search_binary(
        #nums = [4,5,6,7,0,1,2],target = 0
        #nums=[1,3],target=3
        #nums = [1],target = 1
        nums=[5,1,2,3,4],target=1
    )
    print(answer)