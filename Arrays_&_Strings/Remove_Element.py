class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        #numsc = nums doesn't make a new lis, it references to the orignal so put nums[:] or list(nums)
        numsc = nums[:]
        p = 0
        for i in range(len(numsc)):
            if numsc[i] == val:
                nums.remove(nums[p])
                p -= 1
            
            p +=1
        
        return len(nums)

            