class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mergedlength = len(nums1) + len(nums2)
        mergedhalf = mergedlength // 2

        A, B = nums1, nums2

        if len(B) < len(A):
            A, B = B, A

        left, right = 0, len(A) - 1

        while True:
            a = (left + right) // 2
            b = mergedhalf - a - 2

            Aleft = A[a] if a >= 0 else float('-inf')
            Aright = A[a + 1] if a + 1 < len(A) else float('inf')
    
            Bleft = B[b] if b >= 0 else float('-inf')
            Bright = B[b + 1] if b + 1 < len(B) else float('inf')

            if Aleft <= Bright and Bleft <= Aright:
                if mergedlength % 2 == 1:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                right = a - 1
            else:
                left = a + 1
