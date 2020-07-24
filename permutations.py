class Solution:
    def permute(self, nums: list) -> list:
        import itertools
        result = itertools.permutations(nums)
        return list(map(list, result))


a = Solution()
b = a.permute([1, 2, 3])
print(b)
