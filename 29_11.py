# Jump Game III

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        seen = set()
        queue = deque([start])
        while queue:
            pos = queue.popleft()
            seen.add(pos)
            if arr[pos] == 0:
                return True
            for next_pos in [pos + arr[pos], pos - arr[pos]]:
                if 0 <= next_pos < len(arr) and next_pos not in seen:
                    queue.append(next_pos)
        
        return False
        