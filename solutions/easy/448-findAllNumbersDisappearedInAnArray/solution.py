class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # For every number in the array we search the index given that number
        # And mark the index (number) as a negative number
        # Then we iterate over the list again and if the curent number is non
        # negative we add it to our result

        for num in nums:
            index = abs(num) - 1
            nums[index] = - (abs(nums[index]))
        
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)

        return result