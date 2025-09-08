class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count={}
        first={}
        last={}
        for i,num in enumerate(nums):
            if num not in first:
                first[num]=i
            last[num]=i
            count[num]=count.get(num,0)+1
        degree=max(count.values())
        min_len=len(nums)
        for num in nums:
            if count[num]==degree:
                min_len=min(min_len,last[num]-first[num]+1)
        return min_len