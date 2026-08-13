import math
class Solution:
    def isPrime(self, num) -> bool:
        if num == 1:
            return False
        elif num == 2:
            return True
        for i in range(2,int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        primes = {}
        for num in nums:
            if num in primes:
                primes[num] += 1
            else:
                primes[num] = 1
        for k in primes.keys():
            if self.isPrime(primes[k]):
                return True
        return False