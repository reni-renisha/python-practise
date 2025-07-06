
## 🐍 Python Practice Problems

This repository contains Python solutions to coding problems, organized by difficulty level to support step-by-step learning & the questions named lc are from leetcode.

### 🗂️ Folder Overview

* `easy/` — Basic problems using loops, conditions, and lists.  
  Includes:

1.  Write a program that prints the numbers from 1 to 100.
 But for multiples of 3, print "Fizz" instead of the number.
 For multiples of 5, print "Buzz" instead of the number.
 For numbers which are multiples of both 3 and 5, print "FizzBuzz"

    [Answer](easy/fizzbuzz.py)

2.  You’re given an array A of n integers and q queries. Each query can be one of the following two types:  
Type 1 Query: (1, l, r) - Replace A[i] with (i-l+1)*A[l] for each index i, where l <= i <= r.  
Type 2 Query: (2, l, r) - Calculate the sum of the elements in A from index l to r.  
Find the sum of answers to all type 2 queries. Since answer can be large, return it modulo 10^9+7.  
[Answer](easy/p1.py)

3.  You are given an array A of length N and an integer k. It is given that a subarray from l to r is considered good, if the number of distinct elements in that subarray doesn’t exceed k.  Additionally, an empty subarray is also a good subarray and its sum is considered to be zero.  
Find the maximum sum of a good subarray.  
[Answer](easy/p2.py)

4.  You have an oil tank with a capacity of C litres that can be bought and sold by N people.  
The people standing in a queue are served sequentially in the order of array A.  
Some of them want to sell a litre of oil and some of them want to buy a litre of oil and A describes this.  
Here, A[i] = 1 denotes that the person wants to sell a litre of oil and A[i] = -1 denotes that the person wants to buy a litre of oil.  
When a person wants to sell a litre of oil but the tank is full, they cannot sell it and become upset.  
Similarly, when a person wants to buy a litre of oil but the tank is empty, they cannot buy it and become upset.  
Both these cases cause disturbances.  
You can minimize the disturbance by filling the tank initially with a certain X litres of oil.  
Find the minimum initial amount of oil X that results in the least number of disturbances.  
[Answer](easy/p3.py)

   5. Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have 
     exactly one  solution, and you may not use the same element twice. You can return the answer in any order.
     [Answer](easy/lc1.py)


 

  6. In a particular country, each of the N states has a unique two-letter state code, such as KA for Karnataka, TN for Tamil Nadu, and MH for Maharashtra. Every vehicle registered in a state follows a standard license plate format that consists of the two-letter state code, followed by a four-digit number ranging from 0000 to 9999.

   However, certain constraints are applied while issuing license numbers:

- The first digit of the number cannot be 0. For example, numbers such as 0123 are invalid.
- Numbers where all four digits are the same, such as 1111, 2222, 3333, etc., are considered special numbers and are reserved for auctions. These should not be counted.

  Given the number of states and their respective codes, determine the total number of valid license plates that can be issued across all states, excluding special numbers. Write a   simple Python program (no functions) to solve this.
  [Answer](easy/p4.py)


      

* `medium/` — For intermediate problems with more logic (coming soon)

* `hard/` — For advanced problems like DP or recursion (coming soon)

* `README.md` — Overview of the repository

