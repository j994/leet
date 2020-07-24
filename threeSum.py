class Solution:

    def threeSum(self, nums: list) -> list:
        nums.sort()
        final = set()
        for i, v in enumerate(nums[:-2]):
            # if i >= 1 and v == nums[i-1]:
            #     print(i, v)
            #     continue

            d = {}
            for x in nums[i + 1:]:
                if x not in d:
                    d[-v-x] = 1
                else:
                    final.add((v, -v-x, x))
        return list(map(list, final))


test = [-1, 0, 1, 2, -1, -4]
a = Solution()
b = a.threeSum(test)
print(b)
