class Solution:
    def grayCode(self, n: int) -> list[int]:
        ans = [0]

        for i in range(n):
            bit = 1 << i

            for j in range(len(ans) - 1, -1, -1):
                ans.append(ans[j] + bit)
        return ans