class Solution:
    def reverse(self, x: int) -> int:
        strx = ''
        if x < 0:
            strx += '-'
        if abs(x) < 10:
            return strx + str(abs(x))
        
        x = str(abs(x))
        for i in range(len(x)-1,-1,-1):
            if x[i] == '0' and len(strx) < 2:
                if len(strx) == 1:
                   if strx[0] == '-': continue
                elif len(strx) == 0: continue
            strx += x[i]
        
        if len(strx) >= 10:
            if strx[0] == '-':
                if int(strx[1:]) > 2147483647: return 0
            else:
                if int(strx) > 2147483647: return 0
        return strx
        