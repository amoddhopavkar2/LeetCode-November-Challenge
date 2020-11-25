# Smallest Integer Divisible by K

class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if not K % 2:
            return -1
        
        result = 1
        count = 1
        while count <= K:
            if result % K == 0:
                return count
            result = result * 10 + 1
            count += 1
        
        return -1