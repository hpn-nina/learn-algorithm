class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        diction = {}
        recordcol = {}
        for i in range(len(s)):
            char = s[i]
            if char not in diction:
                diction[char] = [i] #If it isn't the character that we have meet, add it into the dictionary with the record of index it is in
                if 0 not in recordcol:
                    recordcol[0] = [i] #Tell us about the column of the index it in
                else: recordcol[0].append(i)
            
            else:    
                diction[char].append(i) #This is a character we have met, add the index in the list we have created before
                col = len(diction[char]) - 1
                if col not in recordcol: recordcol[col] = [i]
                else: recordcol[col].append(i)
                
        #Now we have a dictionary with record of which char appear at which index
        #and a record of which index appear in which col of the dictionary
        
        cols = len(recordcol)
        if cols == 1:
            return len(s)
        
        target = None
        maxi = 0
        for i in range(cols):
            if i == cols - 1: return maxi
            if target == None:
                target = recordcol[1][0]
                maxi = target - recordcol[0][0] 
            else:
                minc = float('inf')
                for j in recordcol[i]:
                    if j >= target and j < minc:
                        minc = j
                        
                if minc < float('inf'):
                    curr = minc
                    minc = float('inf')
                
                    for j in recordcol[i+1]:
                        if j > curr and j < minc:
                            minc = j
                    if minc < float('inf'):
                        target = minc
                        maxi = (maxi if maxi > target-curr + 1 else target-curr)
                        
                
            
        
        