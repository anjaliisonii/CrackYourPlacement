class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        #the absolute value represents its size
        #and sign represents its directions
        #if both abs value is same then both are exploits
        #if two astroids meet then smaller one will exploits
        #ya to https://leetcode.com/problems/asteroid-collision/solution/
        stack = []
        for a in asteroids:
            if a > 0:
                stack.append(a)
            else:
                while stack and stack[-1] > 0 and stack[-1] + a < 0:#lesser will sploits
                    stack.pop()
                if not stack or stack[-1] < 0:
                    stack.append(a)
                elif stack[-1] + a == 0:#(same val)
                    stack.pop()
        return stack