class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.lstrip()
        s=s.rstrip()
        res=s.split()
        res.reverse()
        return " ".join(res)
