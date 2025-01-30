class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        target=999999999999

        for num in nums:
            dis= abs(num)
            if dis < abs(target):
                target = num
            
            if dis == abs(target):
                if num> target:
                    target= num
            

        return target
        
        