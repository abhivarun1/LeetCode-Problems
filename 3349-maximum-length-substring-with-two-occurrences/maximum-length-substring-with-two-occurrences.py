class Solution:
    def counter(self, s: str) -> bool:
        di = {}
        for char in s:
            if char in di:
                di[char] += 1
            else:
                di[char] = 1
        for value in di.values():
            if value > 2:
                return False
        return True
    def maximumLengthSubstring(self, s: str) -> int:
        max_len = 0
        for i in range(len(s)):
            maxed = 0
            for j in range(i,len(s)):
                maxi = self.counter(s[i:j+1])
                mxed = len(s[i:j+1])
                if maxi:
                    if mxed > max_len:
                        max_len = mxed
        return max_len