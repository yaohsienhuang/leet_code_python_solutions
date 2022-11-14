from typing import List, Set, Dict, Tuple, Optional

class Solution:
    '''
    Input: x = 121
    Output: true
    Explanation: 121 reads as 121 from left to right and from right to left.
    '''
    def isPalindrome(self, x: int) -> bool:
        '''
        Runtime: 90 ms, faster than 78.34% of Python3 online submissions for Palindrome Number.
        '''
        x_str=str(x)
        isPal=[ 1 for x in range(len(x_str))]
        for i in range(len(x_str)):
            x_str_i=x_str[i]
            x_str_i_reverse=x_str[-(i+1)]
            if x_str_i==x_str_i_reverse:
                isPal[i]=0
        answer=True if sum(isPal)==0 else False
        return answer
    
    def isPalindrome_shorten(self, x: int) -> bool:
        '''
        Runtime: 138 ms, faster than 36.46% of Python3 online submissions for Palindrome Number.
        '''
        return str(x)[::-1] == str(x)

if __name__ == '__main__':
    answer=Solution().isPalindrome(
        x=121,
    )
    print(answer)