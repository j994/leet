class Solution:
    def moveZeroes(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = []
        for i, num in enumerate(nums):
            while nums[i] == 0:
                nums.pop(i)
                zeros.append(0)
                if i >= len(nums):
                    break
        nums += zeros
        return None


li = [0]
a = Solution()
a.moveZeroes(li)
print(li)
