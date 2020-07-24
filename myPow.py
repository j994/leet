class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            x = 1/x
            n = abs(n)
        num = x
        for y in range(1, n):
            print(x)
            num *= x
        return num


sol = Solution()
a = sol.myPow(2.000, -2)
print(a)
