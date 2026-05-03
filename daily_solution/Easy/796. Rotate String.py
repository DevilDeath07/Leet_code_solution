class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        dq = deque(s)
        n = len(s)

        for _ in range(n):
            rotated = "".join(dq)
            if rotated == goal:
                return True
            dq.rotate(-1) 
        return False
