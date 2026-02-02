class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for i in asteroids:
            alive=True
            while alive and i<0 and stack and stack[-1]>0:
                if stack[-1]<-i:
                    stack.pop()
                    continue
                elif stack[-1]==-i:
                    stack.pop()
                alive=False
            if alive:
                stack.append(i)
        return stack
            
            