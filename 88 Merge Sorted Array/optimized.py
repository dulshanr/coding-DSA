from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p_nums1 = m - 1
        p_nums2 = n - 1

        starting_index = m + n - 1

        while (starting_index >= 0):

            if (p_nums1 < 0):
                nums1[starting_index] = nums2[p_nums2]
                p_nums2 -= 1
                starting_index -= 1
            elif (p_nums2 < 0):
                nums1[starting_index] = nums1[p_nums1]
                p_nums1 -= 1
                starting_index -= 1

            elif (nums1[p_nums1] > nums2[p_nums2]):
                nums1[starting_index] = nums1[p_nums1]
                p_nums1 -= 1
                starting_index -= 1
            else:
                nums1[starting_index] = nums2[p_nums2]
                p_nums2 -= 1
                starting_index -= 1




