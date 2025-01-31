class Solution(object):
    def containsDuplicate(self, nums):
        a=set()
        for num in nums:
            if num not in a:
                a.add(num)
            else:
                return True
        return False