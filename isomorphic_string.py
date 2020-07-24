class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        return (len(set(s)) == len(set(t)) == len(set(zip(s, t))))


a = Solution()
b = a.isIsomorphic('paper', 'title')
print(b)
