class Solution:
    def intToRoman(self, num: int) -> str:
        def convert_to_roman(value):
            val_map = [
                (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
                (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
                (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
            ]
            roman = ""
            for v, symbol in val_map:
                while value >= v:
                    roman += symbol
                    value -= v
            return roman

        # Split num into positional components like [3000, 700, 40, 9]
        digits = [int(d) for d in str(num)]
        n = len(digits) - 1
        for i in range(len(digits)):
            digits[i] *= (10 ** n)
            n -= 1

        # Convert each component to Roman
        roman_parts = [convert_to_roman(val) for val in digits if val > 0]
        final_roman = "".join(roman_parts)
        return final_roman
