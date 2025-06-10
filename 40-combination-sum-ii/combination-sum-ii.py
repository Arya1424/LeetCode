class Solution(object):
    def combinationSum2(self, candidates, target):
        result = []
        candidates.sort()  # Sorting helps avoid duplicate combinations
        
        def backtrack(start, path, total):
            if total == target:
                result.append(list(path))
                return
            elif total > target:
                return  # Stop if sum exceeds target
            
            for i in range(start, len(candidates)):
                # Avoid picking the same element multiple times in one loop level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                path.append(candidates[i])
                backtrack(i + 1, path, total + candidates[i])  # Move to next index
                path.pop()
        
        backtrack(0, [], 0)
        return result
