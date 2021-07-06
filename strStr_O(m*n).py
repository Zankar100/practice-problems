class Solution:      
    def strStr(self, haystack: str, needle: str) -> int:
        M = len(needle)
        N = len(haystack)
        
        # A loop to slide pat[] one by one
        if M == 0:
            return 0
        
        for i in range(N - M + 1):
 
            counter = 0
            # For current index i,
            # check for pattern match
            for j in range(M):
                if (haystack[i + j] != needle[j]):
                    break
                else:
                    counter += 1
             
            if counter == M :
                return i
 
        return -1