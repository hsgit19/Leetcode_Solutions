class Solution:
    def isValid(self, s: str):
        hmap = {'(' : ')',
                '{' : '}',
                '[' : ']'}

        stack = []

        for strng in s:
            if strng in hmap:
                stack.append(strng)
            else:
                if len(stack) == 0:
                     return False
                elif hmap[stack[-1]] != strng:
                    return False
                else:
                    stack.pop()
        return len(stack) == 0
    