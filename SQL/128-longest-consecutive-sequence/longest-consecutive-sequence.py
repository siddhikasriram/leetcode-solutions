class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ans = 0

        nums = set(nums)

        for i in nums: 
            if i-1 not in nums: 
                count = 0
                while i+count in nums: 
                    count += 1 
                    ans = max(ans, count)
        return ans




        