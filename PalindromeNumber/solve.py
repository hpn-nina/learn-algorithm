class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True

        x = str(x)
        length = len(x)

        if length % 2 == 0:
            pat1, pat2 = (length//2)-1,length//2
        else:
            pat1, pat2 = (length//2)-1,(length//2)+1

        while pat1 >= 0:
            if x[pat1] != x[pat2]:
                return False
            pat1, pat2 = pat1-1, pat2+1
        return True    
                
        