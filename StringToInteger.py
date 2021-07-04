class Solution:
    def myAtoi(self, s: str) -> int:
        
        s=s.lstrip()
        
        i = 0
        result = 0
        maxnum = 2 ** 31 - 1
        minnum = -2 ** 31
        sign = 1
        
        if i<len(s) and s[i] == '-':
            sign = -1
            i += 1
        elif i<len(s) and s[i] == '+':
            i += 1
        
        while i < len(s) and s[i].isnumeric():
            result = result*10 + int(s[i])
            i += 1
        
        result = result * sign
        
        if result < 0:
            return max(minnum, result)
        else:
            return min(maxnum, result)
        
        