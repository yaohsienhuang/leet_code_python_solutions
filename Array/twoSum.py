from typing import List, Set, Dict, Tuple, Optional

class Solution():
    '''
    Difficulty: Easy
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
    '''
    def twoSum(self, nums:List[int], target:int) -> List[int]:
        dict={}
        for idx,value in enumerate(nums):
            if target-value in dict:
                return [dict[target-value],idx]
            dict[value]=idx


if __name__ == '__main__':
    answer=Solution().twoSum(
        nums=[2,7,11,15],
        target= 9
    )
    print(answer)