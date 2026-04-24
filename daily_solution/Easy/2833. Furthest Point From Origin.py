class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        def compute_distance(moves, replace_char):
            arr = list(moves)
            k = 0
            for i in range(len(arr)):
                if arr[i] == replace_char or arr[i] == "_":
                    arr[k] = replace_char
                    k += 1
                else:
                    arr[k] = arr[i]
                    k += 1
            result = 0
            for m in arr:
                if m == "L":
                    result -= 1
                elif m == "R":
                    result += 1
            return abs(result)

        # Try underscores as L and as R
        distL = compute_distance(moves, "L")
        distR = compute_distance(moves, "R")

        return max(distL, distR)
