class Solution(object):
    def combinationSum(self, candidates, target):
        #backtracking
        result=[]
         
        def backtrack(start,path,total):
            if target==total:
                result.append(list(path))
                return
            elif total>target:
                return
            
            for i in range(start,len(candidates)):
                path.append(candidates[i])
                backtrack(i,path,total+candidates[i])
                path.pop()
            
        backtrack(0,[],0)
        return result
        

        