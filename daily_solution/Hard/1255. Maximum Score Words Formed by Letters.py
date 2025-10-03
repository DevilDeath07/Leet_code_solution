class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        # Step 1: Eliminate zero scores and build mapping
        letter_score = {}
        for i in range(26):
            if score[i] != 0:
                letter_score[chr(i + ord('a'))] = score[i]

        # Step 2: Score each word using the filtered mapping
        count = []
        for word in words:
            temp = 0
            for ch in word:
                temp += letter_score.get(ch, 0)  # Safe access
            count.append(temp)

        # Step 3: Prepare for combination scoring
        letter_count = Counter(letters)
        n = len(words)
        max_score = 0

        def can_form(combo):
            total = Counter()
            for word in combo:
                total += Counter(word)
            for ch in total:
                if total[ch] > letter_count.get(ch, 0):
                    return False
            return True

        def score_combo(combo):
            return sum(letter_score.get(ch, 0) for word in combo for ch in word)

        # Step 4: Try all combinations
        for r in range(1, n + 1):
            for combo in combinations(words, r):
                if can_form(combo):
                    max_score = max(max_score, score_combo(combo))

        # Step 5: Output result
        return max_score
