class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        if target in nums:
            return nums.index(target)
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        for i, num in enumerate(nums):
            if nums[i] < target < nums[i+1]:
                return i + 1


a = Solution()
b = a.searchInsert([1, 3, 5, 6], 2)
print(b)
