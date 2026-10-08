class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # treat 2d matrix as a flattened array and try
        
        size = len(matrix) * len(matrix[0])
        # print(size)

        i = 0
        j = size - 1

        while i <= j:
            middle =  (i+j) // 2
            m = middle // len(matrix[0])
            n = middle - (m*len(matrix[0]))
            # print(m, n, matrix[m][n]), above is for finding corresponding index in the 2d matrix
            if target == matrix[m][n]:
                return True

            elif target < matrix[m][n]:
                j = middle - 1

            else:
                i = middle + 1

        return False