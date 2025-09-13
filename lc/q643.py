class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: float
        :rtype: float
        """
        l=len(nums)
        currSum=0
        for i in range(k):
            currSum+=nums[i]
        max_avg=float(currSum)/k
        for i in range(k,l):
            currSum+=nums[i]
            currSum-=nums[i-k]
            avg=float(currSum)/k
            max_avg=max(max_avg,avg)
        return max_avg