class Solution:
    def commonChars(self, A: list) -> list:
        from collections import Counter
        c = Counter(A[0])
        for i in range(1, len(A)):
            w = Counter(A[i])
            c = c & w
        return list(c.elements())


a = Solution()
b = a.commonChars(["cool", "lock", "cook"])
print(b)
