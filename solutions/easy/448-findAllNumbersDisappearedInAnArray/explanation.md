# 448 - Find All Numbers Disappeared in an Array
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]
 

Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
 

Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

## Initial Thoughts
- Get the length of nums
- Create a set using nums list
- Use a for loop from i=0 to the length of nums 
    - If the current i + 1 is not in the set
        - Add it to the result
- return result

### Improvement
- Although the time complexity is O(n), space complexity is also O(n) due to the set. 
- Instead of using extra DS, we can use the list that was given by marking the numbers that have appeared by turning the number into the corresponding index negative
- Then we can iterate over the marked array and just add non-negative numbers to the result