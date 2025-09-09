class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count=0
        for start in range(len(nums)):
            total=0
            for end in range(start,len(nums)):
                total+=nums[end]
                if total==k:
                    count+=1
        return count

        #another solution i tried for increased optimization and to learn hashmap

        class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        curr_sum=0 #to keep track of sum of numbers till now
        prefixSum={0:1}#to keep track of the count of prefix sums
        res=0

        for n in nums:#iterate through each number
            curr_sum+=n#add it to curr_sum
            diff=curr_sum-k#take the diffrence of curr_sum and k ,so that if we find this diff in prefixSum it means we have found a subarray with sum k
            res+=prefixSum.get(diff,0)#from the hashmap take the count of that prefixsum and add it to result,that 0 is default value if diff not found
            prefixSum[curr_sum]=1+prefixSum.get(curr_sum,0)#update the count of curr_sum in the hashmap
        return res
