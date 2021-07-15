class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        
        #can use => count = collections.Counter(s)
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = 1
            else:
                d[s[i]] += 1
        
        #can use enumerate
        for i in range(len(s)):
            if d[s[i]] == 1:
                return i
        
        return -1