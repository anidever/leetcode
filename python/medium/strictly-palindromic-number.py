# # question can be found on leetcode.com/problems/strictly-palindromic-number/

class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        size = len(str(n))
        
        def isPalindromic(num):
            return num == num[::-1]
        
        def numberToBase(num, base):
            if num == 0:
                return [0]

            digits = []
            while num:
                digits.append(int(num % base))
                num //= base
                
            return digits[::-1]
            
            
        
        for base in range(2, n-1):
            if not isPalindromic(numberToBase(n, base)):
                return False
        
        return True
