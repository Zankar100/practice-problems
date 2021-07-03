class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        maxlen = 0
        zdict = {}
        
        while end < len(s):
            if s[end] in zdict and zdict[s[end]] >= start:
                start = zdict[s[end]] + 1
            maxlen = max(maxlen, end - start + 1)
            zdict[s[end]] = end
            end += 1
        
        return maxlen