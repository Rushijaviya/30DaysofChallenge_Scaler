# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        d={'[':']','{':'}','(':')'}
        stack=[]
        for i in s:
            if i in '([{':
                stack.append(d[i])
            else:
                if stack and stack.pop()==i:
                    continue
                return False
        return not stack