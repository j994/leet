class Solution:
    def frequencySort(self, s: str) -> str:
        result = ''
        count = {}
        for c in s:
            if c not in count:
                count[c] = 1
            else:
                count[c] += 1
        final = sorted(count.items(), key=lambda x: x[1], reverse=True)

        for item in final:
            result += item[0] * item[1]
        return result

    def freq2(self, s: str):
        from collections import Counter
        return ''.join([char * times for char, times in Counter(s).most_common()])


a = Solution()
b = a.freq2('tree')
print(b)
