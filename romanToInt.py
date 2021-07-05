class Solution:
    def romanToInt(self, s: str) -> int:
        value = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
        }
        
        p = 0
        res = 0
        
        n = len(s)
        
        for i in range(n-1, -1, -1):
            if value[s[i]] >= p:
                res += value[s[i]]
            else:
                res -= value[s[i]]
            
            p = value[s[i]]
            
        return res
        