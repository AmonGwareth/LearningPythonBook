
class Solution:

    def __init__(self):
        self.data = []
        self.len = 0

    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        self.data = sorted(nums1 + nums2)
        self.len = len(self.data)

        if self.len % 2 == 0:
            idx = int(self.len/2)
            return (self.data[idx - 1] + self.data[idx]) / 2
        else:
            idx = int((self.len - 1) / 2)
            return self.data[idx]

