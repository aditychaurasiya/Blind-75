class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        for i in range(length):
            if i not in nums:
                return i
                break
        else:
            return length
                

        