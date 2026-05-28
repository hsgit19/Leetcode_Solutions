class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                    continue

            lft = i + 1
            rght = len(nums) - 1

            while lft < rght:

                total = nums[i] + nums[lft] + nums[rght]

                if total == 0:
                    result.append([nums[i], nums[lft], nums[rght]])
                    lft += 1
                    rght -= 1
                    while lft < rght and nums[lft] == nums[lft - 1]:  
                         lft += 1
                elif total > 0:
                    rght -= 1
                else:
                    lft += 1
                
            
        return result

        