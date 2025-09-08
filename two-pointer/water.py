...
Container With Most Water

Given height[], find two lines that hold the most water.

Example:
Input: [1,8,6,2,5,4,8,3,7]
Output: 49  
...

def maxArea(height):
    left=0
    right=len(height)-1
    max_water=0
    while left<right:
        width=right-left
        water=width*min(height[left],height[right])
        if water>max_water:
              max_water=water
        if height[left]<height[right]:
             left+=1 
        else:
              right -=1 
    return max_water
nums=list(map(int,input().split()))
print(maxArea(nums))
