class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1 or s == s[::-1]:
            return s
        else:
            max_len = 1
            start = 0
            for i in range(1, len(s)):
                odd = s[i - max_len - 1: i + 1]
                even = s[i - max_len: i + 1]
                if i - max_len - 1 >= 0 and odd == odd[::-1]:
                    start = i - max_len - 1
                    max_len = max_len + 2
                    continue
                if even == even[::-1]:
                    start = i - max_len
                    max_len = max_len + 1
        return s[start: start + max_len]


if __name__ == '__main__':
    s = 'abbacb'
    c = Solution()
    print(c.longestPalindrome(s))