class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        test = str.split(' ')

        if len(test) != len(pattern):
            return False

        return (len(set(pattern)) == len(set(test)) == len(set(zip(pattern, test))))


a = Solution()
b = a.wordPattern('aba', 'cat cat cat dog')
print(b)
