class Solution:
    def twoSum(self, nums: List[int], target: int):

      d = {}

      for i in range (len(nums)):
         curr_num = nums[i]
         compl = target - curr_num

         if compl in d:
            return [d[compl], i]
         else:
            d[curr_num] = i


       



        