import math
class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:

        start = math.isqrt(l)
        if start * start < l:
            start += 1
        end = math.isqrt(r)
        
        if start > end:
            return r - l + 1

        is_prime = [True] * (end + 1)
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(end ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, end + 1, i):
                    is_prime[j] = False
        count = 0
        for i in range(start,end + 1):
            if is_prime[i] == True:
                count += 1
        return (r - l + 1) - count
