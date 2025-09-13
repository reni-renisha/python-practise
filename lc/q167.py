class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left=0#start pointer
        right=len(number)-1#end pointer
        while left<right:
            currSum=numbers[left]+numbers[right]
            if currSum>target:
                right-=1
            elif currSum<target:
                left-=1
            else:
                return [left+1,right+1]#since index start at 1