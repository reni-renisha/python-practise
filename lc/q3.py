class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left=0
        uniq=set()
        max_len=0
        for right in range(len(s)):
            while s[right] in uniq:
                uniq.remove(s[left])
                left+=1
            uniq.add(s[right])
            if right-left+1>max_len:
                max_len=right-left+1
                start_index=left
        return max_len
        