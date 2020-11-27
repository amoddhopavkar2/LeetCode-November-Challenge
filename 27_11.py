#  Partition Equal Subset Sum

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False

        target = sum(nums) // 2
        dp = [0] * (target * 2)
        dp[0] = 1
        for num in nums:
            if num > target:
                return False 
            if num == target:
                return True
            
            for i in range(target, -1, -1):
                if dp[i] == 1:
                    dp[i+num] = 1
                if dp[target]:
                    return True
        
        return False
        