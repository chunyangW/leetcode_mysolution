class Maxheap:
    # 使用数组，并从索引0开始存储堆中元素
    def __init__(self):
        self.max_heap = []
    # 查询堆顶元素
    def peek(self):
        if self.max_heap:
            return self.max_heap[0]
        else:
            return None
    # 插入新元素到大顶堆的数组最末尾并进行上滤操作保持大顶堆
    def push(self, val):
        self.max_heap.append(val)
        size = len(self.max_heap)

        self.__shift_up(size - 1)
    def __shift_up(self, i):
        while (i - 1) // 2 >= 0 and self.max_heap[i] > self.max_heap[(i - 1) // 2]:   # //是地板除，/除法输出的就是四舍五入的浮点数
            self.max_heap[i], self.max_heap[(i - 1) // 2] = self.max_heap[(i - 1) // 2], self.max_heap[i]
            i = (i - 1) // 2
        
    # 弹出堆顶元素并维持大顶堆（最大堆）
    def pop(self):
        if not self.max_heap:
            raise IndexError("heap is empty")
        # 先将最后一个与第一个对调，然后使用数组的pop()函数将最后一个元素弹出然后将 根节点的元素shift_down
        size = len(self.max_heap)
        self.max_heap[0], self.max_heap[size - 1] = self.max_heap[size - 1], self.max_heap[0]
        val = self.max_heap.pop()
        size -= 1
        # 下滤操作额外size的大小
        self.__shift_down(0, size)
        return val
    def __shift_down(self, i, size):
        # 与上滤操作相同的是需要一个终止条件就是 当前的左子节点要小于等于size那么就能在往下降一层
        while 2 * i + 1 < size:
            # 先计算出左右子节点的索引 索引关系 （i-1）// 2 ， i， 2* i+ 1， 2*i + 2
            left, right = 2 * i + 1, 2 * i + 2
            # 下面就是找到字节点中较大的一个值，如果是当前父节点大于较大字节点那么就不需要再进行下滤操作了
            # 但是如果只有左节点就直接将较大的赋值给左节点
            # 同时如果父节点大于较大子节点那么就将他们两个交换
            if right >= size:
                lager = left
            else:
                if self.max_heap[left] <= self.max_heap[right]:  # 其实如果是smaller并且i更大的两个那就要将更小的放上去，形成小顶堆（下面）
                    lager = right
                else:
                    lager = left
            # 对于大顶堆，如果下面两个中有一个更大，那么就需要将更大的作为父，小顶堆相反需要去找下面两个中更小的
            if self.max_heap[i] < self.max_heap[lager]:
                self.max_heap[i], self.max_heap[lager] = self.max_heap[lager], self.max_heap[i]
                i = lager
            else:
                break 
    # 利用上面的基本算法建立大顶堆并进行堆排序
    def __build_maxheap(self, array):
        # 先将数组中的元素提交到大顶堆中然后从最后一个非叶子节点开始下滤操作？
        # 首先最下面的叶节点是不需要进行下滤的
        # 同时从最后一个非叶子节点下滤可以使得每个节点只需要进行一次下滤操作（从下到上逐步确保每个子树都满足大顶堆的性质）小顶堆类似
        size = len(array)
        for i in range(size):
            self.max_heap.append(array[i])
        start = (size - 1 - 1) // 2 # size - 1是最后一个节点， 那么它上面的父节点(i - 1 // 2)就是最后一个非叶字节点
        for i in range(start, -1, -1):  # 从start 到 -1 但是 - 1 取不到，同时步长为 -1 那么- 1的前一个就是 0
            self.__shift_down(i,size)
    # 堆排序
    def heapsort(self, nums):
        self.__build_maxheap(nums)
        size = len(self.max_heap)
        print(f"initial max heap: {self.max_heap}")

        for i in range(size - 1, -1, -1):
            # 交换根节点与当前堆的最后一个节点
            self.max_heap[0], self.max_heap[i] = self.max_heap[i], self.max_heap[0]
            # 从根节点开始，对当前堆（不包括已经放在最后的元素了）进行下移调整
            self.__shift_down(0, i)   
        # 返回排序后的数组
        return self.max_heap

# 下面对功能进行测试：
class Solution:
    def sortArray(self, nums):
        return Maxheap().heapsort(nums)

a = Solution()
print(a.sortArray([10, 25, 6, 8, 7, 1, 20, 23]))


