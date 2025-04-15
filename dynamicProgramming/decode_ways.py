# 91. Decode Ways

class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        n = len(s)
        prev = 1
        curr = 1

        for i in range(1, n):
            temp = 0

            if s[i] != '0':
                temp += curr

            two_digit = int(s[i-1:i+1])

            if (10 <= two_digit <= 26):
                temp += prev

            prev, curr = curr, temp

            if curr == 0:
                return 0
        return curr
