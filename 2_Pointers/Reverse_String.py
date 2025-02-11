class Solution(object):
    def reverseString(self, s):

        l = 0
        r = len(s) - 1
        lis = []

        while l < r:
            temp = s[l]
            s[l] = s[r]
            print s[l]
            s[r] = temp
            print s[r]

            l += 1
            r -= 1
        
        return s
    

'''
class Solution(object):
    def reverseString(self, s):
        return s.reverse()


'''