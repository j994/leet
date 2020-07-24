class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        for i in range(2, len(cost)):
            cost[i] += min(cost[i-1], cost[i - 2])
            print(i)
        return min(cost[-1], cost[- 2])


test = [0, 0, 1, 1]
a = Solution()
b = a.minCostClimbingStairs(test)
print(b)
