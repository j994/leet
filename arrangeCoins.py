class Solution:
    def arrangeCoins(self, n: int) -> int:
        coins = n
        row = 1
        while coins:
            coins -= row
            if coins < row + 1:
                return row
            row += 1
        return row


a = Solution()
b = a.arrangeCoins(11)
print(b)
