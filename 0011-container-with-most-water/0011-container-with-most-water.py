class Solution:
    def maxArea(self, height: List[int]):

        l1 = 0
        l2 = len(height) - 1
        max_area = 0

        while l1 < l2:
            area = (l2 - l1)*(min(height[l1], height[l2]))

            max_area = max(area,max_area)
                 
            if height[l1] < height[l2]:
                l1 += 1
            else:
                l2 -= 1

        return max_area

       
                

          

            
        