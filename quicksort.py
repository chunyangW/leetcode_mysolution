import random

class Solution():
    def sortarray(self, nums):
        def quicksort(nums, left, right):
            pivot = nums[random.randint(left,right)]     # 随机取哨兵大小使得在最差的有序情况下也能实现 O(n logn)
            i,j = left, right                            # 左右向中间移动将异常值移到左右然后使得i j同时移动到哨兵的位置
            while i <= j:                                # 等于是为了当最后左右索引相等时实现i,j从哨兵处离开从而划分
                while nums[j] > pivot:                   # 只去找小于的值 但是最终要在Pivot处停下所以不能等于pivot
                    j -= 1   
                while nums[i] < pivot:
                    i += 1
                if i<=j:                                  # 只有当i <= j才能去交换
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1                                # 继续前行
                    j -= 1   
            if i<right: quicksort(nums,i,right)           # 分而治之
            if j>left: quicksort(nums,left,j)                   
        quicksort(nums,0,len(nums)-1)
        return nums


   
    

# 测试
a = Solution()
array = [1,2,43,4,1,3,0]
a.sortarray(array)
print(array)