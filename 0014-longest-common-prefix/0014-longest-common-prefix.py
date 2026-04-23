class Solution:
    def longestCommonPrefix(self, strs: List[str]):
        OUT = ""
        for j in range(max(len(s) for s in strs)):
            for i in range(len(strs)):
                if len(strs[i]) <= j:
                    return OUT
                if strs[i][j] != strs[0][j]:
                    return OUT
            OUT += strs[0][j]
        return OUT


        