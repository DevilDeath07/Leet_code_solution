from collections import deque

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        def add_to_odd_indices(s, a):
            s = list(s)
            for i in range(1, len(s), 2):
                s[i] = str((int(s[i]) + a) % 10)
            return ''.join(s)

        def rotate(s, b):
            return s[-b:] + s[:-b]

        visited = set()
        queue = deque([s])
        min_string = s

        while queue:
            current = queue.popleft()
            if current in visited:
                continue
            visited.add(current)
            if current < min_string:
                min_string = current

            # Apply addition to odd indices
            added = add_to_odd_indices(current, a)
            if added not in visited:
                queue.append(added)

            # Apply rotation
            rotated = rotate(current, b)
            if rotated not in visited:
                queue.append(rotated)

        return min_string
