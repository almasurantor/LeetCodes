class Solution(object):
    def longestCommonPrefix(self, strs):
        word=""
        small=strs[0]
        bk=False
        for wordi in strs:
            if len(wordi) < len(small):
                small=wordi
    
        for i in range(len(small)):
            letter= small[i]
        
            for wordi in strs:
                if wordi[i] != letter:
                    bk=True
            if bk:
                break
            else:
                word+= letter
            
        print(word)
        
        return word