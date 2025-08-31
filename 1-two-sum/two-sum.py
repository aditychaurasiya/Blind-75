class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            temp = nums[i]
            for j in range(i+1, n):
                if nums[j] == target - temp:
                    return [i, j]
        return []
