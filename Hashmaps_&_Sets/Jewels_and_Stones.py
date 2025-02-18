class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """

        jew = set(jewels)
        count = 0
        for letter in stones:
            if letter in jew:
                count += 1
        
        return count

    