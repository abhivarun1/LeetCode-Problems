class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        sieve = [True] * n
        sieve[0] = False
        sieve[1] = False

        for i in range(2,int(n**0.5) + 1):
            if sieve[i] == True:
                for j in range(i*i,n,i):
                    sieve[j] = False
        return sum(sieve)