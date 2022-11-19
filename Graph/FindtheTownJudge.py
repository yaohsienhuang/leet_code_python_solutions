from typing import List

class Solution:
    '''
    Input: n = 3, trust = [[1,3],[2,3]]
    Output: 3
    '''
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        '''
        Runtime: 2010 ms, faster than 21.64% of Python3 online submissions for Find the Town Judge.
        '''
        trusted = [0] * (n+1)
        for a, b in trust:
            trusted[a] -= 1
            trusted[b] += 1

        for i in range(1, n+1):
            if trusted[i] == n-1:
                return i
        return -1
    
    def findJudge_best(self, n: int, trust: List[List[int]]) -> int:
        '''
        Runtime: 884 ms, faster than 80.83% of Python3 online submissions for Find the Town Judge.
        '''
        if n == 0: return -1
        graph = {}
        for i in range(1,n+1):
            graph[i] = set()
        # {1: set(), 2: set(), 3: set(), 4: set()}
        
        for e in trust:
            graph[e[0]].add(e[1])
        # {1: {3, 4}, 2: {3, 4}, 3: set(), 4: {3}}
        
        candidates = [i for i,v in graph.items() if len(v) == 0]
        # [3]
        if len(candidates) == 0: return -1
        candidate = candidates[0]
        
        # everyone must trust candidate, except for the town judge
        for i,v in graph.items():
            if candidate == i: continue
            if candidate not in graph[i]:
                return -1
        
        return candidate


if __name__ == '__main__':
    answer=Solution().findJudge_best(
        #n = 2, trust = [[1,2]],
        #n = 3, trust = [[1,3],[2,3]],
        #n = 3, trust = [[1,2],[2,3]],
        n = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
    )
    print(answer)