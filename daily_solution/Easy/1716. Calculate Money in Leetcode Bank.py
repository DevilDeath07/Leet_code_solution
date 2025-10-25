class Solution:
    def totalMoney(self, n: int) -> int:
        # Calculate money with dynamic chunking
        def split_into_chunks(lst, chunk_size=7):
            return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]
        currency = [i for i in range(1, n + 1)]

        # Step 2: Split into chunks of size 7
        split_list = split_into_chunks(currency)

        # Step 3: Update each chunk based on the first element of the previous chunk
        for i in range(1, len(split_list)):
            start = split_list[i - 1][0] + 1
            split_list[i] = [start + j for j in range(len(split_list[i]))]
        #step 4: sum of all splited list
        result = 0
        for i in split_list:
            result += sum(i)
        return result
