class Solution(object):
    def myAtoi(self, s):
        if not s:
            return 0
        s=s.lstrip()
        if not s:
            return 0
        sign=1
        i=0
        num=0
        INT_MAX,INT_MIN=2**31-1,-2**31
        if s[0]=='-':
            sign=-1
            i=1
        elif s[0]=='+':
            i=1
        l=0
        while i<len(s) and s[i].isdigit():
            digit=int(s[i])
            if num>(INT_MAX-digit)//10:
                return INT_MAX if sign==1 else INT_MIN
            num=num*10+digit
            i+=1
        return sign*num