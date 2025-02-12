class Solution(object):
    def isPalindrome(self, s):
        
        """
        left = 0
        right = len(s)-1
     

        while left < right:
            if not s[left].isalnum():
                left += 1
            if not s[right].isalnum():
                right -=1
            
            if s[right].isalnum() and s[left].isalnum():
                if s[left].lower() != s[right].lower():
                    return False
                
                left += 1
                right -=1
            
        
        return True
        """
        
        """
        news = ""

        for letter in s:
            if letter.isalnum():
                news += letter
        
        news = news.lower()

        return news == news[::-1]

        """

        s = re.sub(r"[^a-zA-Z0-9]", "", s)  
        s = s.lower() 

        return s == s[::-1]  