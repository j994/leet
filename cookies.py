class Solution:
    def findContentChildren(self, g: list, s: list) -> int:
        g.sort()
        s.sort()
        count = 0
        cookie = 0
        while cookie < len(s) and count < len(g):
            if s[cookie] >= g[count]:
                count += 1
            cookie += 1

        return count


a = Solution()
b = a.findContentChildren([1, 2, 3], [1, 1])
print(b)
