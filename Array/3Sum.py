from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        correct! but the time Limit Exceeded
        '''
        result = []
        if nums.count(0) >= 3:
            result.append([0, 0, 0])
        sorted_nums = sorted(nums)
        for i in range(len(sorted_nums)-2):
            n1=sorted_nums[i]
            for j in range(i+1,len(sorted_nums)):
                n2=sorted_nums[j]
                n3=-(n1+n2)
                if n3 in sorted_nums[j+1:]:
                    if [n1,n2,n3] not in result:
                        result.append([n1,n2,n3])
        return result

    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        '''
        Runtime 624 ms
        Beats 97.91%
        '''
        result = []
        nums.sort()
        n=len(nums)
        for i in range(n-2):
            # [0,1,2,3...] without negative value
            if nums[i]+nums[i+1]+nums[i+2]>0:
                break
            # [-50,...,2,3] too big negative value
            if nums[i]+nums[n-1]+nums[n-2]<0:
                continue
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            l,r=i+1,n-1
            while l<r:
                sum=nums[i]+nums[l]+nums[r]
                if sum==0:
                    result.append([nums[i],nums[l],nums[r]])
                    while l+1<r and nums[l]==nums[l+1]:
                        l+=1
                    l+=1
                    while l<r-1 and nums[r]==nums[r-1]:
                        r-=1
                    r-=1
                elif sum<0:
                    l+=1
                else:
                    r-=1
        return result
    
    def threeSum3(self, nums: List[int]) -> List[List[int]]:
        '''
        Runtime 433 ms
        Beats 99.57%
        '''
        result = []
        if nums.count(0) >= 3:
            result.append([0, 0, 0])
        seen = set()
        visited = set(x for x in nums if x in seen or seen.add(x))
        deduped = sorted(set(nums))
        for i, n in enumerate(deduped[:-1]):
            for n2 in deduped[i + 1:]:
                n3 = -(n2 + n)
                if n3 in visited and (n >= n3 or n3 == n2):
                    result.append([n, n2, n3])
            visited.add(n)
        return result
            
            
if __name__ == '__main__':
    answer=Solution().threeSum2(
        nums=[-1,0,1,2,-1,-4],
        #nums=[-1,0,1,0],
        #nums=[0,1,1],
        #nums=[0,0,0],
    )
    print(answer)