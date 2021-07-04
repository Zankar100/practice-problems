class Solution:
    def intToRoman(self, num: int) -> str:
        romansDict = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M"
        }
        
        div = 1
        
        while num >= div:
            div *= 10
        
        div /= 10
        
        result = ''
        
        while num:
            
            signum = int(num/div)
            
            if signum < 4:
                result += (romansDict[div]*signum)
            elif signum == 4:
                result += (romansDict[div] + romansDict[div*5])
            elif 5 <= signum < 9:
                result += (romansDict[div*5] + romansDict[div]*(signum-5))
            elif signum == 9:
                result += (romansDict[div] + romansDict[div*10])
            
            num = num % div
            div /= 10
        
        return result
