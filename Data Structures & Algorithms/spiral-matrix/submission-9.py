class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        res = []

        while True:
            for j in range(left, right + 1):
                res.append(matrix[top][j])
            top += 1
            if top > bottom:
                break
            
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            if right < left:
                break
            
            for j in range(right,left - 1, -1):
                res.append(matrix[bottom][j])
            bottom -= 1
            if top > bottom:
                break

            for i in range(bottom,top - 1, -1):
                res.append(matrix[i][left])
            left += 1
            if right < left:
                break
        
        return res


        