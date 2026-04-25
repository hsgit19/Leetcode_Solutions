from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]):
        cst = Counter(nums)

        for c in cst:
            if cst[c] > len(nums)/2:
               return c
            

        