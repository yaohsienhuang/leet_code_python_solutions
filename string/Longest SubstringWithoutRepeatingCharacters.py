class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        Runtime 52 ms
        Beats 97.32%
        '''
        used = {}
        max_length = 0
        start = -1
        for i, key in enumerate(s):
            print(f'i={i}; start={start}; key={key}; used={used}')
            if key in used and start <= used[key]:
                start = used[key]
                used[key] = i
            else:
                max_length = max(max_length, i - start)
                used[key] = i
            print(f'max={max_length}; used={used}')
        return max_length
        
if __name__ == '__main__':
    answer = Solution().lengthOfLongestSubstring(
        s="abcabcbb"
    )
    print(answer)