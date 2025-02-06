class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        dic={}

        for letter in magazine:
            if letter not in dic:
                dic[letter]=1
            else:
                dic[letter]+=1
        
        for letter in ransomNote:
            if letter in dic and dic[letter] !=0:
                dic[letter] -=1
            else:
                return False
        return True