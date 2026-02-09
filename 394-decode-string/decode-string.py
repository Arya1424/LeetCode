class Solution:
    def decodeString(self, s: str) -> str:
        num=[]
        stack=[]
        n=0
        res=""
        for i in s:
            if i.isdigit():
                n=n*10+int(i)
            elif i=="[":
                num.append(n)
                stack.append(res)
                res=""
                n=0
            elif i=="]":
                repeat=num.pop()
                prev=stack.pop()
                res=prev+res*repeat
            else:
                res+=i
        return res