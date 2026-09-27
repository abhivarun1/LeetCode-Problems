class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res = 0
        
        for i in range(32):
            bit_count = 0
            for num in nums:
                if num & (1 << i) != 0:
                    bit_count += 1
            if bit_count % 3 == 1:
                res = res | (1 << i)
        if res & (1 << 31):
            res -= (1 << 32)
        return res