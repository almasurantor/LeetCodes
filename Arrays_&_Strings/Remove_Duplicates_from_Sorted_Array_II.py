class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        numscopy = nums[:]

        for word in numscopy:
            if nums.count(word) > 2:
                nums.remove(word)
        
        return len(nums)

        """
        much better appoarch 

        if not nums:
            return 0

        k = 0  # Pointer to track position
        for num in nums:
            if k < 2 or nums[k - 2] != num:
                nums[k] = num
                k += 1
        
        return k

        """