class Solution(object):
    def isSubsequence(self, s, t):
        if s == "":
            return True
        string=""
        count=0
        for item in t:
            if item == s[count] and count < len(s):
                string+=item
                count+=1
            if string==s:
                return True
        return False