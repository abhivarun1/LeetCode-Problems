class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        seted = set(nums)
        res = []

        for i in range(1,len(nums)+1):
            if i not in seted:
                res.append(i)
        return res