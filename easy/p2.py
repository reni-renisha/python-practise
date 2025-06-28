#You are given an array A of length N and an
#integer k.
##It is given that a subarray from l to r is considered
#good, if the number of distinct elements in that
#subarray doesn’t exceed k. Additionally, an empty
#subarray is also a good subarray and its sum is
#considered to be zero.
#Find the maximum sum of a good subarray.
n = int(input())  # number of elements in the list
k = int(input())  # max distinct numbers allowed
A = list(map(int, input().split()))  # list of integers
from collections import defaultdict #0 by default, instead of giving an error
def max_sub(A,k):
    left=0 #start index of current subarray
    count=defaultdict(int)
    curr_sum=0 #current total
    max_sum =0#highest sum till now
    for right in range(len(A)):  # loop from start to end
        num=A[right]
        count[num] += 1
        curr_sum += num
        while len(count)>k: # if unique numbers exceed
         left_num=A[left]
         count[left_num]-=1
         curr_sum-= left_num
         if count[left_num] == 0:
          del count[left_num]
         left += 1
        max_sum = max(max_sum, curr_sum)
    return max_sum
print(max_sub(A, k))#print result





