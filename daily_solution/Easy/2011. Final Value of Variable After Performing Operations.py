class Solution:
    def finalValueAfterOperations(self, operations):
        x = 0
        for op in operations:
            if op == "++X" or op == "X++":
                x += 1
            if op == "--X" or op == "X--":
                x -= 1
        return x
