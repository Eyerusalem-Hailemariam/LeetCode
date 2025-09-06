class Node:
    def __init__(self, val):
        self.val = val
        self.prev = self.next = None
class MyLinkedList:

    def __init__(self):

        self.left, self.right = Node(0), Node(0)
        self.left.next, self.right.prev = self.right, self.left

    def get(self, index: int) -> int:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        
        if cur and cur != self.right and index == 0:
            return cur.val
        return -1
    def addAtHead(self, val: int) -> None:
        node = Node(val)
        prev, nxt = self.left, self.left.next
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev
    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.left.next

        while cur and index > 0:
            cur = cur.next
            index -= 1

        if cur and index == 0:
            node = Node(val) 
            prev, nxt = cur.prev, cur 
            prev.next = nxt.prev = node
            node.next, node.prev = nxt, prev
        

    def deleteAtIndex(self, index: int) -> None:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1

        if cur and cur != self.right and index == 0:
            prev, nxt = cur.prev, cur.next 
            prev.next, nxt.prev = nxt, prev
        
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)