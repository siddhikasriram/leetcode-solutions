class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pm =k
        set(nums)
        for i in range (0, len(nums)):
            if pm not in nums:
                return pm
            pm +=k
            
        return pm

