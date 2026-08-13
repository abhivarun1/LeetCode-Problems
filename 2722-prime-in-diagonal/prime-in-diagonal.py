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
            maxi = 0
            if (nums[i][i] > res) and (nums[i][i] % 2 != 0 or nums[i][i] == 2):
                maxi = self.isPrime(nums[i][i])
                if maxi > res:
                    res = maxi
            if (nums[i][len(nums) - i - 1] > res) and (nums[i][len(nums) - i - 1] % 2 != 0 or nums[i][len(nums) - i - 1] == 2):
                maxi = self.isPrime(nums[i][len(nums) - i - 1])
                if maxi > res:
                    res = maxi
        return res