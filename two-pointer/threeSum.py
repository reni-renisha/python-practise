...
Three Sum

Return all unique triplets [a,b,c] such that a+b+c=0.

Example:
Input: [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
...
def threeSum(nums):
    res=[]
    for i in range(len(nums)-2):
        if i>0 and nums[i]==nums[i-1]:
            continue

        left=i+1
        right=len(nums)-1
        while left<right:
            s=nums[i]+nums[left]+nums[right]
            if s==0:
                res.append([nums[i],nums[left],nums[right]])
                while left<right and nums[left]==nums[left+1]:
                    left+=1 
                while left<right and nums[right]==nums[right-1]:
                    right-=1 
                left += 1
                right -= 1
            elif s>0:
                right-=1 
            else:
                left+=1

    return res

n=list(map(int,input().split()))
nums=sorted(n)
print(threeSum(nums))