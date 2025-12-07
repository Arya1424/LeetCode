class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res=[]
        def backtrack(string, i):
            if i==len(s):
                res.append("".join(string))
                return
            ch=s[i]
            if ch.isalpha():
                backtrack(string+ch.lower(), i+1)
                backtrack(string+ch.upper(), i+1)
            else:
                backtrack(string+ch, i+1)

        backtrack('',0)
        return res


        