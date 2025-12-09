class Solution:
    def isValid(self, s: str) -> bool:
        p={')':'(', ']':'[', '}':'{'}
        stack=[]
        for i in s:
            if stack and i in p and stack[-1]==p[i]:
                stack.pop()
            else:
                stack.append(i)
        return not stack
        