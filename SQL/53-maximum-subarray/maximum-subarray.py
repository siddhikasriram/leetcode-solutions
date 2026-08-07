class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #base case 

        if len(nums) == 1:
            return nums[0]
        
        dp = [0] * len(nums)

        for i in range(0, len(nums)):
            if i ==0:
                dp[0] = nums[i]
            else:
                dp[i] = max(nums[i], nums[i]+ dp[i-1])
        
        return max(dp)