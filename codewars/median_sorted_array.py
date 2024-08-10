import statistics
from typing import List
import numpy as np
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        longer_array, shorter_array = (nums1, nums2) if len(nums1) > len(nums2) else (nums2, nums1)
        search_idx = int(np.floor(len(longer_array)/2))
        search_array = []
        for i, x in enumerate(shorter_array):
            print(search_idx)
            print(longer_array)
            inserted = False
            if (search_idx == len(longer_array)-1):
                longer_array = longer_array + shorter_array[i:]
                break
            while not inserted:
                if x >= longer_array[search_idx]:
                    if x <= longer_array[search_idx+1]:
                        longer_array.insert(search_idx+1, x)
                        inserted = True
                    search_array = longer_array[search_idx:]
                    search_idx = int(search_idx + np.floor((len(longer_array) - search_idx) / 2))
                else:
                    if x >= longer_array[search_idx-1]:
                        longer_array.insert(search_idx, x)
                        inserted = True
                    search_array = longer_array[:search_idx+1]
                    search_idx = int(np.floor(search_idx / 2))

        return statistics.median(longer_array)


sol = Solution()
sol.findMedianSortedArrays([2,2,4,4], [2,2,4,4])
