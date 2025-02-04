class Solution(object):
    def twoSum(self, nums, target):
        

        for i in range(len(nums)):
            for z in range(len(nums)):
                if nums[i] + nums[z] == target and i !=z:
                    return [i,z]