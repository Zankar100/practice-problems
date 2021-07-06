class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        difference = float('inf')
        nums.sort()
        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if abs(target - sum) < abs(difference):
                    difference = target - sum
                if sum < target:
                    l += 1
                else:
                    r -= 1
            if difference == 0:
                break
                
        return target - difference