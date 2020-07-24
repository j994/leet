class Solution:
    def intersect(self, nums1: list, nums2: list) -> list:
        from collections import Counter
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        return list((c1 & c2).elements())


a = Solution()
b = a.intersect([1, 2, 2, 1], [2, 2])
print(b)
