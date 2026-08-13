class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        res = set()
        for num in nums:
            while num % 2 == 0:
                res.add(2)
                num //= 2
            for i in range(3,int(sqrt(num)) + 1, 2):
                while num % i == 0:
                    res.add(i)
                    num //= i
            if num > 2:
                res.add(num)
        return len(res)