"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, 
but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, 
where the first m elements denote the elements that should be merged, 
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""


class SolutionError(Exception): ...


def merge(nums1: list[int], nums2: list[int]) -> None:
    i, j = len(nums1), len(nums2)
    while i and j:
        if nums1[0] > nums2[0]:
            nums1.append(nums2.pop(0))
            j -= 1
        else:
            nums1.append(nums1.pop(0))
            i -= 1
    if i:
        nums1 = nums1[i:] + nums1[:i]
    elif j:
        nums1 += nums2
