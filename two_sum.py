class Solution:
    def twoSum(self, nums, target: int):
        num = {}
        for i, x in enumerate(nums):
            complete = target - x
            if complete in num:
                return [num[complete], i]
            num[x] = i
            print(num)
        return []


a = Solution()
b = a.twoSum([3, 7, 13, 1, 19], 14)
print(b)
