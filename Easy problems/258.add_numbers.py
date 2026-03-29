# Easy problem

class Solution:
    def addDigits(self, num: int) -> int:
        sum = 0
        while len(str(num)) != 1:
            for i in str(num):
                sum += int(i) 
            num = sum
            sum = 0
        return num
    
S = Solution
print(S.addDigits(S,38))