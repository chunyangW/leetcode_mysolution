<<<<<<< HEAD
# 用快速排序
import random
from typing import List

class Solution:
    def inventoryManagement(self, stock: List[int], cnt: int) -> List[int]:
        def quickselect(nums, l, r):
            pivot_i = random.randint(l, r)
            nums[l], nums[pivot_i] = nums[pivot_i], nums[l]
            i, j = l, r
            while i < j:   # 保证nums[i], nums[j]处相等时即使下面的条件满足最后两个哨兵也是停在一起 
                while(nums[j] >= nums[l] and i < j):   
                    j -= 1
                while(nums[i] <= nums[l] and i < j):   # 确保最终停下来的地方左边都是严格小于等于哨兵的
                    i += 1
                nums[i], nums[j] = nums[j], nums[i]
            nums[l] , nums[i] = nums[i], nums[l]  # 最后将哨兵放在正确的地方
            # 因为题目对于最左边返回的顺序没有要求那么只要哨兵的位置 i >= cnt - 1 时?? 并不是已经找到了 必须要 i == cnt -1 啊
            if i < cnt - 1 and i + 1 < r:
                return quickselect(nums, i+1, r)
            if i > cnt - 1 and l < i - 1:   
                return quickselect(nums, l, i-1)
            
        if cnt >= len(stock): 
            return stock
        
        quickselect(stock, 0, len(stock) - 1)
        return stock[:cnt]

a = Solution()
print(a.inventoryManagement([2,5,7,4], 1))
=======
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
>>>>>>> 2126b80b98c3260562d13ec1484a1aeff33b43f6
