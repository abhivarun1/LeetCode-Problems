class Solution:
    def smallestValue(self, n: int) -> int:
        while(1):
            fact_sum = 0
            temp = n

            while temp % 2 == 0:
                fact_sum += 2
                temp //= 2
            i = 3

            while i * i <= temp:
                while temp % i == 0:
                    fact_sum += i
                    temp //= i
                i += 2
            if temp > 2:
                fact_sum += temp
            
            if fact_sum == n:
                return fact_sum
            n = fact_sum