class Solution:
    def bitwiseComplement(self, n: int) -> int:
        binary = format(n,'b')
        complement = (''.join('1' if bit == '0' else '0' for bit in binary)).strip()
        comp_int = int(complement,2)
        return comp_int
