class Solution(object):
    def myAtoi(self, s):
        s=s.lstrip()
        if not s:
            return 0
        sign,i,result=1,0,0
        n=len(s)

        if  s[0]=="-":
            sign=-1
            i+=1
        elif s[0]=="+":
            i+=1
        
        INT_MAX,INT_MIN=2**31-1,-2**31

        while i<n and s[i].isdigit():
            digit=int(s[i])
            if result > (INT_MAX-digit)//10:
                return INT_MAX if sign==1 else INT_MIN
            result=result*10+digit
            i+=1
        return sign*result