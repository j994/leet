class Solution:
    def convertToBase7(self, num: int) -> str:
        exp = 8
        final = []
        neg_flag = False
        if num < 0:
            neg_flag = True
        test = abs(num)
        while exp >= 0:
            divisor = pow(7, exp)
            i, test = divmod(test, divisor)
            print(test, i, divisor)
            final.append(str(i))
            exp -= 1
        ans = str(int(''.join(final)))
        if neg_flag:
            return '-' + ans
        return ans


a = Solution()
b = a.convertToBase7(
    10000000)
print(b)
