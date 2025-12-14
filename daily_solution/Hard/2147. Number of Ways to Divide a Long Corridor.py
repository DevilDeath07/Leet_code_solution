class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 7

        seats = []
        for i, ch in enumerate(corridor):
            if ch == "S":
                seats.append(i)

        # Step 1: If seats are odd or zero → no way
        if len(seats) == 0 or len(seats) % 2 != 0:
            return 0

        ways = 1

        # Step 2: Process seat pairs
        for i in range(2, len(seats), 2):
            plants_between = seats[i] - seats[i - 1] - 1
            ways = (ways * (plants_between + 1)) % MOD
        return ways
