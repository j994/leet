class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        import math
        factors = [1]
        high = math.ceil(math.sqrt(num))
        for x in range(2, high):
            if num % x == 0:
                factors.append(x)
                factors.append(int(num/x))
        print(factors)
        if num == sum(factors):
            return True
        return False


a = Solution()
b = a.checkPerfectNumber(6)
print(b)
