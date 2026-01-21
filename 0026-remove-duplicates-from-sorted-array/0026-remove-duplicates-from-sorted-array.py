class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        
        i = 0
        for j in range(i, len(nums)):
            if nums[i] < nums[j]:
                nums[i + 1] = nums[j]
                i+=1
        return i + 1
