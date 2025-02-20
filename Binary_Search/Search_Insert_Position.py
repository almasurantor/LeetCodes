class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        p1 = 0
        p2 = 0

        while p1 < len(nums):
            if nums[p1] == target:
                return p1
            
            if nums[p1] < target:
                p2 += 1

            p1 += 1
        
        return p2