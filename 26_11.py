# Longest Substring with At Least K Repeating Characters

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) == 0 or k > len(s):
            return 0
        
        cnt = Counter(s)
        sub1, sub2 = '', ''
        for i, letter in enumerate(s):
            if cnt[letter] < k:
                sub1 = self.longestSubstring(s[:i], k)
                sub2 = self.longestSubstring(s[i+1:], k)
                break
        else:
            return len(s)
        
        return max(sub1, sub2)
        