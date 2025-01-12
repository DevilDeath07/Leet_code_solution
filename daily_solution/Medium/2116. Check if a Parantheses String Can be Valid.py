class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s)%2==1:
            return False
        #because odd length string is not balanced by the paranthesis
        openBrackets=[]
        unlocked=[]
        for i in range(len(s)):
            if locked[i]=="0":
                unlocked.append(i)
            elif s[i] =="(":
                openBrackets.append(i)
            elif s[i]==")":
                if openBrackets:
                    openBrackets.pop()
                elif unlocked:
                    unlocked.pop()
                else:
                    return False
        while openBrackets and unlocked and openBrackets[-1] < unlocked[-1]:
            openBrackets.pop()
            unlocked.pop()
        if openBrackets:
            return False
        return True
