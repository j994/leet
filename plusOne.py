class Solution:
    def plusOne(self, digits: list) -> list:
        test = int(''.join(list(map(str, digits))))
        test += 1
        return list(map(int, list(str(test))))


a = Solution()
b = a.plusOne([9, 9])
print(b)
