class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = [[]]

        for num in nums:
            new = [curr + [num] for curr in res]
            res.extend(new)
        return res