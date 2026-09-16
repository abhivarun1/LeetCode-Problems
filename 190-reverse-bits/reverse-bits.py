class Solution:
    def reverseBits(self, n: int) -> int:
        num = bin(n)[2:].zfill(32)
        rev = str(num)[::-1]
        res = int(rev,2)

        return res