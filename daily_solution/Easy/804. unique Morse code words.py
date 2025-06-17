class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
         "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
         "..-", "...-", ".--", "-..-", "-.--", "--.."]
        
        for i in range(len(words)):
            words[i] = words[i].upper()

        # Array to store Morse codes of each letter

        result = []
        for i in range(len(words)):
            morse_array = []
            for ch in words[i]:
                index = letters.index(ch)      # Find index of the letter
                code = morse[index]            # Get Morse code from the list
                morse_array.append(code)       # Store it in array

            result1 = ''.join(morse_array)
            result.append(result1)
        
        final = set(result)

        return len(final)
