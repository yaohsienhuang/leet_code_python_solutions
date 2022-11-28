from typing import List

class Solution:
    '''
    Input: prices = [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
    '''
    def maxProfit(self, prices: List[int]) -> int:
        '''
        Time Limit Exceeded	
        '''
        max_profit=0
        length=len(prices)
        for i in range(length):
            for j in range(i+1,length):
                profit=prices[j]-prices[i]
                if profit>max_profit:
                    max_profit=profit
        return max_profit
            
    def maxProfit2(self, prices: List[int]) -> int:
        '''
        Runtime: 2657 ms, faster than 39.47% of Python3 online submissions for Best Time to Buy and Sell Stock.
        '''
        left = 0
        right = 1
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left]
            if prices[left] < prices[right]:
                max_profit =max(currentProfit,max_profit)
            else:
                left = right
            right += 1
        return max_profit

    def maxProfit3(self, prices: List[int]) -> int:
        '''
        Runtime: 1223 ms, faster than 80.66% of Python3 online submissions for Best Time to Buy and Sell Stock.
        '''
        max_profit = 0
        minPurchase = prices[0]
        for i in range(1, len(prices)):		
            max_profit = max(max_profit, prices[i] - minPurchase)
            minPurchase = min(minPurchase, prices[i])
        return max_profit
            

if __name__ == '__main__':
    answer=Solution().maxProfit3(
        prices = [7,1,5,3,6,4],
        #prices = [7,6,4,3,1],
    )
    print(answer)