...
two sum but sorted and with two pointers
...
def twoSum(sort,target):
    left=0
    right=len(sort)-1
    while left<right:
        s=sort[left]+sort[right]
        if s==target:
            return(sort[left],sort[right])
        elif s>target:
            right-=1 
        else:
            left+=1 
nums=list(map(int,input().split()))
target = int(input())
arranged=sorted(nums)
print(twoSum(nums,target))