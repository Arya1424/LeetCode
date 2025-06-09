class Solution(object):
    def isValid(self, s):
        stack=[]
        brackets={"(":")","{":"}","[":"]"}
        for i in s:
            if i in brackets:
                stack.append(i)
            elif i in brackets.values():
                if not stack or brackets[stack.pop()]!=i:
                    return False
            else:
                return False
        return len(stack)==0