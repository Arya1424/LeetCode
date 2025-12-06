class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        mindiff=float('inf')
        arr.sort()
        res=[]
        for i in range(1,len(arr)):
            mindiff=min(mindiff,arr[i]-arr[i-1])
            
        for i in range(1,len(arr)):
            if mindiff==arr[i]-arr[i-1]:
                res.append([arr[i-1],arr[i]])
        return res
        