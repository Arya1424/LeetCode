class Solution(object):
    def combinationSum3(self, k, n):
        result=[]

        def backtrack(curr, k, n, start):
            if k==0 and n==0:
                result.append(list(curr))
                return
            if k<0 or n<0:
                return 
            for i in range(start, min(10, n+1)):
                backtrack(curr +[i], k-1, n-i, i+1)

            
        backtrack([], k, n, 1)
        return result


            
        