class Solution:
    def maxProfit(self, prices: list) -> int:
        maxCurr, maxTot = 0, 0
        for i in range(1, len(prices)):
            temp = maxCurr + prices[i] - prices[i-1]
            maxCurr = max(0, temp)
            maxTot = max(maxCurr, maxTot)
            print(maxCurr, maxTot)
        return maxTot


a = Solution()
b = a.maxProfit([7, 1, 5, 3, 6, 4])
print(b)
