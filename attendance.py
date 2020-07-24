class Solution:
    def checkRecord(self, s: str) -> bool:
        count = 0
        if len(s) < 3:
            count += s.count('A')
        for i in range(1, len(s) - 1):
            if i == 1:
                if s[i - 1] == 'A':
                    count += 1
            if s[i-1] == s[i] == s[i + 1] == 'L':
                return False
            if s[i] == 'A':
                count += 1
        if count > 1:
            return False
        print(count)
        return True


a = Solution()
b = a.checkRecord('AA')
print(b)
