import math
class Solution:
    def isPrime(self, num) -> int:
        if num == 1:
            return 0
        elif num == 2:
            return 2
        for i in range(2,int(math.sqrt(num)) + 1):
            if num % i == 0:
                return 0
        return num
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        res = 0
        for i in range(len(nums)):
            for val in (nums[i][i], nums[i][len(nums) - i - 1]):
                if val > res and (val % 2 != 0 or val == 2):
                    maxi = self.isPrime(val)
                    if maxi > res:
                        res = maxi
        return res