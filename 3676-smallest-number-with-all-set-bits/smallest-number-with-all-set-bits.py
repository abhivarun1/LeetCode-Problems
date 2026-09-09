class Solution:
    def smallestNumber(self, n: int) -> int:
        while(1):
            if (n & (n+1) == 0):
                return n
            n += 1