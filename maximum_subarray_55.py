#dp 1d array with each slot being the max subarray ending at that number since subarrays are contiguous this is possible

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0] * len(nums)
        max_sum = nums[0]
        dp[0] = nums[0]
        for i in range(1,len(nums)):
            if(nums[i] + dp[i-1] > nums[i]):
                dp[i] = nums[i] + dp[i-1]
                max_sum = max(dp[i], max_sum)
            else:
                dp[i] = nums[i]
                max_sum = max(dp[i], max_sum)
            
        return max_sum
