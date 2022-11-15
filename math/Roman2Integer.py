from typing import List, Set, Dict, Tuple, Optional

class Solution:
    '''
    Input: s = "LVIII"
    Output: 58
    Explanation: L = 50, V= 5, III = 3.
    '''
    dict={'I' : 1,'V' : 5,'X' : 10,'L' : 50,'C' : 100,'D' : 500,'M' : 1000}
    replace_dict={"IV":"IIII","IX": "VIIII","XL": "XXXX","XC":"LXXXX","CD":"CCCC","CM":"DCCCC"}
    
    def romanToInt(self, s: str) -> int:
        '''
        Runtime: 93 ms, faster than 57.58% of Python3 online submissions for Roman to Integer.
        '''
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        return sum([self.dict[i] for i in s])
    
    def romanToInt_loopSum(self, s: str) -> int:
        '''
        2.Runtime: 83 ms, faster than 69.69% of Python3 online submissions for Roman to Integer.
        '''
        for key,value in self.replace_dict.items():
            s=s.replace(key,value)
        number=0
        for j in s:
            number += self.dict[j]
        return number
        
if __name__ == '__main__':
    answer=Solution().romanToInt_loopSum(
        s='MCMXCIV',
    )
    print(answer)