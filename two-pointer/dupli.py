...
Remove Duplicates from  Array using two pointers
...

#used a slow pointer na dfast pointer ,all the unique elements are at the start of the array,
#fast pointer traverses the array and slow pointer only moves when a new element is found
def dupli(nums):
    i=0
    l=len(nums)
    for j in range(1,l):
        if nums[i]!=nums[j]:
            i+=1
            nums[i]=nums[j]
    return i+1
            

n=list(map(int,input().split()))
nums=sorted(n)
leng=dupli(nums)
print(leng)#length
print(nums[:leng])#numbers till length needed