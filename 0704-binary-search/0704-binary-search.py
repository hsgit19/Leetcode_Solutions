class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lft = 0
        rght = len(nums) - 1
        

        while lft <= rght :
            mid = (lft + rght) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
               rght = mid - 1
            else:
                lft = mid + 1
        
        return -1
            

