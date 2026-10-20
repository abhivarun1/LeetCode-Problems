class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        temp = sorted(nums)
        hash_map = {}
        res = []
        for i,v in enumerate(temp):
            if v not in hash_map:
                hash_map[v] = i
        for i in nums:
            res.append(hash_map[i])
        return res