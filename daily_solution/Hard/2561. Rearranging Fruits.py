class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        Two_array = basket1 + basket2
        freq = Counter(Two_array)
        all_even = all(count % 2 == 0 for count in freq.values())
        if all_even:
            freq1 = Counter(basket1)
            freq2 = Counter(basket2)
            surplus1 = []
            surplus2 = []

            for val in freq:
                diff = freq1[val] - freq2[val]
                if diff > 0:
                    surplus1.extend([val] * (diff // 2))
                elif diff < 0:
                    surplus2.extend([val] * (-diff // 2))
            surplus1.sort()
            surplus2.sort(reverse=True)
            min_val = min(freq)
            cost = 0
            for x, y in zip(surplus1, surplus2):
                swap_cost = min(2 * min_val, min(x, y))
                cost += swap_cost

            return cost
        else:
            return -1
