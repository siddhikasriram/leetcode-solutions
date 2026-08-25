class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [None]*(len(nums))
        #base 
        if len(nums) <3:
            return max(nums)
        else:
            dp[0] = nums[0]
            dp[1] = max(nums[0],nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i] , dp[i-1])
        return dp[-1]



        