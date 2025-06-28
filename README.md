
## 🐍 Python Practice Problems

This repository contains Python solutions to coding problems, organized by difficulty level to support step-by-step learning.

### 🗂️ Folder Overview

* `easy/` — Basic problems using loops, conditions, and lists.
  Includes:
  1.
   [ Answer](easy/fizzbuzz.py)
  2.You’re given an array A of n integers and q queries.Each query can be one of the following two types:Type 1 Query: (1, l, r) - Replace A[i] with(i-l+1)*A[l]
    for each index i, where l <= i <= r. Type 2 Query: (2, l, r) - Calculate the sum of the elements in A from index l to index r.Find the sum of answers to all type 2 queries.
    Since answer can be large, return it modulo 10^9+7.
      [Answer](easy/p1.py)
  3.You are given an array A of length N and an integer k.It is given that a subarray from l to r is considered good, if the number of distinct elements in that subarray
    doesn’t exceed k. Additionally, an empty subarray is also a good subarray and its sum is considered to be zero.Find the maximum sum of a good subarray.
    [Answer](easy/p2.py)
  4.You have an oil tank with a capacity of C litres that can be bought and sold by N people. The people standing in a queue are served sequentially in the order of array A.
  Some of them want to sell a litre of oil and some of them want to buy a litre of oil and A describes this.Here, A[i] = 1 denotes that the person wants to sell a litre of oil
   and A[i] = -1 denotes that the person wants to buy a litre of oil.When a person wants to sell a litre of oil but the tank is full, they cannot sell it and become upset .Similarly,
   when a person wants to buy a litre of oil but the tank is empty, they cannot buy it and become upset. Both these cases cause disturbances.You can minimize the
   disturbance by filling the tank initially with a certain X litres of oil.Find the minimum initial amount of oil X that results in the least number of disturbances.
    [Answer](easy/p3.py)

      

* `medium/` — For intermediate problems with more logic (coming soon)

* `hard/` — For advanced problems like DP or recursion (coming soon)

* `README.md` — Overview of the repository

