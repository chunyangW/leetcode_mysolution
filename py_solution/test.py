## just for test
from typing import List
import random

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mid = len(nums) // 2

        def quicksort(l, r):
            pivot = nums[random.randint(l,r)]
            i, j = l, r
            while i <= j:
                while nums[i] < pivot:
                    i += 1
                while nums[j] > pivot:
                    j -= 1
                if i <= j:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j -= 1

            if i <= mid <= r: return quicksort(i,r)
            if l <= mid <= j: return quicksort(l,j)
            return nums[mid]
        
        return quicksort(0, len(nums)-1)
    
a = Solution()
print(a.majorityElement([3,2,3]))