class Solution:
    def majorityElement(self, nums: List[int]):
        can = None
        count = 0

        for num in nums:
            if can == num:
                 count += 1
            elif count == 0:
                 can = num
            else:
                count -= 1

        return can
                 
        

       
            

        