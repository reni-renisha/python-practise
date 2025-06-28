#You’re given an array A of n integers and q queries.
#Each query can be one of the following two types:
#• Type 1 Query: (1, l, r) - Replace A[i] with
#(i-l+1)*A[l] for each index i, where l <= i <= r.
#• Type 2 Query: (2, l, r) - Calculate the sum of the
#elements in A from index l to index r.
#Find the sum of answers to all type 2 queries. Since
#answer can be large, return it modulo 10^9+7.
MOD=10**9+7 #for large output
n=int(input()) #take integer input
A=[int(input()) for _ in range(n)]  # ask the user for a number, convert it to an int, put it in the list
q=int(input()) #number of queries
queries=[]#to store commands
for _ in range(q):
    query=list(map(int,input().split()))#take input and split and turn it into numbers
    queries.append(query)#adds this query into the queries list
total=0#to store final ans
for query in queries:
    t,l,r=query#break into 3 parts
    if t==1: #query 1
        for i in range(l,r+1): #due to index,r+1
            A[i]=A[i] = (i - l + 1) * A[l] #given equation
    elif t==2: #query 2
        total += sum(A[l:r+1]) #Add all values from index l to r
        total %= MOD # keeps the number small and safe
print(total)




