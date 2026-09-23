class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        b = []

        for i in range(len(nums)):
            b.append(nums[nums[i]])

        return  b