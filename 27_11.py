#  Partition Equal Subset Sum

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False

        key = sum(nums) // 2
        dp = [0] * (key * 2)
        dp[0] = 1
        for num in nums:
            if num > key:
                return False 
            
            if num == key:
                return True
            
            for i in range(key, -1, -1):
                if dp[i] == 1:
                    dp[i+num] = 1
                
                if dp[key]:
                    return True
        
        return False
        