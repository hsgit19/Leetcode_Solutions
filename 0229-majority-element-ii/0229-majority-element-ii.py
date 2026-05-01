class Solution:
    def majorityElement(self, nums: List[int]) :
        
        can1 = None
        can2 = None
        count1 = 0
        count2 = 0
        
        for num in nums:
            if can1 == num:
                count1 += 1
            elif can2 == num:
                count2 += 1
            elif count1 == 0:
                can1 = num
                count1 = 1
            elif count2 == 0:
                can2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        
        result = []
        
        if nums.count(can1) > len(nums) / 3:
            result.append(can1)

        if nums.count(can2) > len(nums) / 3:
            result.append(can2)

        return result
     
        

       

            

               
        