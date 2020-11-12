# Permutations II

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        
        nums.sort()
        
        s = [[]]
        for n in nums:
            t = []
            for l in s:
                for i in range(len(l)+1):
                    t.append(l[:i]+[n]+l[i:])
                    if i<len(l) and l[i]==n:
                        break
            s = t
        
        return s
        