class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        numrow = len(matrix)
        numcol = len(matrix[0])
        targetrow = -1

        top, bottom = 0, numrow - 1

        while top <= bottom:
            midrow = (top + bottom) // 2

            if matrix[midrow][0] > target:
                bottom = midrow - 1
            elif matrix[midrow][numcol - 1] < target:
                top = midrow + 1
            else:
                targetrow = midrow
                break

        if targetrow != -1:
            left, right = 0, numcol - 1

            while left <= right:
                mid = (left + right) // 2

                if matrix[midrow][mid] > target:
                    right = mid - 1
                elif matrix[midrow][mid] < target:
                    left = mid + 1
                else:
                    return True

        return False