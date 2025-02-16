class Solution(object):
    def productExceptSelf(self, nums):
        
        
        """
        total = 1
        count = 0
        for num in nums:
            if num != 0:
                total *= num
            else:
                count += 1
        
        if count > 1:
            return [0 for num in nums]


        multlis = []

        for num in nums:

            if count == 0:
                multlis.append(total/num)
            
            else:
                if num == 0:
                    multlis.append(total)
                else:
                    multlis.append(0)
        
        return multlis

        """
        # Better response
        
        length = len(nums)
        before = 1
        after = 1

        result = [0] * length

        for i in range(length):
            result[i] = before
            before *= nums[i]
        
    
        for i in range(length-1, -1, -1):
            result[i] *= after
            after *= nums[i]
        
        return result