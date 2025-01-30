class Solution(object):
    def romanToInt(self, s):
        dic= {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
        sum=0
        i=0
        while i<len(s):
            if i != len(s)-1:
                if dic[s[i]] >= dic[s[i+1]]:
                    sum += dic[s[i]]
                    i+=1
                elif dic[s[i]] < dic[s[i+1]]:
                    sum += dic[s[i+1]]-dic[s[i]]
                    i+=2
            else:
                sum+=dic[s[i]]
                i+=1
        return sum