class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_arr=nums[0]
        max_sum=nums[0]
        for num in nums[1:]:
            curr_arr=max(num,curr_arr+num)
            max_sum=max(curr_arr,max_sum)
        return max_sum