class LinkedNode():
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Bubble_Sort():
    def run(self, head: LinkedNode)-> LinkedNode:
        
        # tail是已排序的链表尾部， node_j排序中移动的指针，node_i是遍历一整遍到结尾，所以移动到最后所需要的次数就是链表节点数
        node_j = head  
        node_i = head
        tail = None

        while node_i:
            node_j = head # 每次外循环后，要从头开始冒泡
            while node_j != tail and node_j.next != tail:  # 尾部已排序所以后面不用去了
                if node_j.val > node_j.next.val:
                    node_j.val, node_j.next.val = node_j.next.val, node_j.val
                node_j = node_j.next
            tail = node_j  
            node_i = node_i.next
        return head
    
array = [5, 3, 4, 2, 5, 7, 1]
head = LinkedNode(array[0])
cur = head
for i in range(1, len(array)):
    node = LinkedNode(array[i])
    cur.next = node
    cur = cur.next

test = Bubble_Sort()
head = test.run(head)
cur = head
while cur:
    print(cur.val, end="->")
    cur = cur.next

print("None")