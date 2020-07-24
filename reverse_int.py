class Solution:
    def reverse(self, x: int) -> int:
        max_32 = 2147483647
        test = str(x)
        li = list(test)
        li.reverse()
        if li[-1] == '-':
            li.insert(0, '-')
            li.pop(-1)
        c = int(''.join(li))
        if abs(c) >= max_32:
            return 0
        return c


a = Solution()
print(a.reverse(120))
