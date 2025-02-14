class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        hasset = set()
        i = 0
        while i < len(nums):
            if nums[i] not in hasset:
                hasset.add(nums[i])
            else:
                nums.pop(i)
                i -= 1
            i += 1
            
        return len(nums)+1