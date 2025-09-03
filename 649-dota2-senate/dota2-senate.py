class Solution(object):
    def predictPartyVictory(self, senate):
        senate=list(senate)
        D,R=deque(),deque()

        for i,elem in enumerate(senate):
            if elem=="R":
                R.append(i)
            else:
                D.append(i)
        
        while D and R:
            Dturn=D.popleft()
            Rturn=R.popleft()
            if Dturn<Rturn:
                D.append(Rturn+len(senate))
            else:
                R.append(Dturn+len(senate))
        return "Dire" if D else "Radiant"
        