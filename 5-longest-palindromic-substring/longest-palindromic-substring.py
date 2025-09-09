class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        start, max_len = 0, 1  # at least one char is palindrome

        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # after loop, [left+1:right] is the palindrome
            return left + 1, right - left - 1

        for i in range(len(s)):
            # Odd length
            l1, len1 = expandAroundCenter(i, i)
            # Even length
            l2, len2 = expandAroundCenter(i, i + 1)

            if len1 > max_len:
                start, max_len = l1, len1
            if len2 > max_len:
                start, max_len = l2, len2

        return s[start:start + max_len]
