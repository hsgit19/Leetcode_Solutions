from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        cnt = Counter(nums)
        n = len(nums)
        Buckets = [0]*(n+1)

        for val, freq in cnt.items():
            if Buckets[freq] == 0:
                Buckets[freq] = [val]
            else:
                Buckets[freq].append(val)   
        res = []
        for i in range(n, -1, -1):
            if Buckets[i] != 0:
                res.extend(Buckets[i])
            if len(res) == k:
                break

        return res
      
        

  

       
        