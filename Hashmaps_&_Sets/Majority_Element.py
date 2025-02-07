class Solution(object):
    def majorityElement(self, nums):
        dic={}
        
        for num in nums:
            if num not in dic:
                dic[num]=1
            else:
                dic[num]+=1
        
        a=0
        ans=0
        for key, value in dic.items():
            if value >a:
                a=value
                ans=key
        
        return ans
