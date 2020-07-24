class Solution:
    def reverseString(self, s: list) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()


test = ["h", "e", "l", "l", "o"]
a = Solution()
a.reverseString(test)
print(test)
