class Solution:
    def isHappy(self, n: int) -> bool:
        trial = n
        for x in range(100):
            test = str(trial)
            trial = sum([int(d)**2 for d in test])
            if trial == 1:
                return True
        return False


a = Solution()
b = a.isHappy(19)
print(b)
