class Solution:
    def isAnagram(self, s: str, t: str):

        ds = {}
        for ls in s:
            ds[ls] = ds.get(ls, 0) + 1
        
        dt = {}
        for lt in t:
            dt[lt] = dt.get(lt, 0) + 1
        
        if len(s) != len(t):
            return False
        else:
            if ds == dt:
               return True
            return False