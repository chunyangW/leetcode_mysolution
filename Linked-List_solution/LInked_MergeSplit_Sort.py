class LinkedNode():
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

'''
首先使用快慢指针，快指针每次移动两个，慢指针每次移动一个，当快指针到最后慢指针也移动到中间了

感觉使用链表解决归并排序非常简单自然
'''
class Split_Merge_Sort():
    def merge(self, lefthead: LinkedNode, righthead: LinkedNode)-> LinkedNode:
        dummy_head = LinkedNode(0)
        cur = dummy_head
        while lefthead and righthead:
            if lefthead.val < righthead.val:
                cur.next = lefthead
                lefthead = lefthead.next
            else:
                cur.next = righthead
                righthead = righthead.next
            cur = cur.next
        # 然后将剩下来的直接接到cur后面就好了
        if lefthead:
            cur.next = lefthead
        elif righthead:
            cur.next = righthead

        return  dummy_head.next

    def split(self, head = LinkedNode)-> LinkedNode:
        if not head or not head.next:  # 如果终止条件为一个，那么最后会在一个的地方无限循环slow
            return head
        
        slow, fast = head, head.next # 一开始fast比slow快一个
        # 找中间
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        righthead = slow.next
        lefthead = head
        slow.next = None  # 断开

        return self.merge(self.split(lefthead), self.split(righthead))


# 验证：

array = [5, 3, 4, 2, 5, 7, 1]
head = LinkedNode(array[0])
cur = head
for i in range(1, len(array)):
    node = LinkedNode(array[i])
    cur.next = node
    cur = cur.next

test = Split_Merge_Sort()
head = test.split(head)
cur = head
while cur:
    print(cur.val, end="->")
    cur = cur.next

print("None")