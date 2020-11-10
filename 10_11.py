# Flipping an Image

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for row in A:
            i, j = 0, len(row) - 1
            while i <= j:
                row[i] , row[j] , i , j = 1^row[j] , 1^row[i] , i+1 , j-1 
        return A
        