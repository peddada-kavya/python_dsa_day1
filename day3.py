#double linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DoubleLinkedList:
    def __init__(self):
        self.head=None
    def add_node(self,data):
        node=Node(data)
        if not self.head:
            self.head=node
        else:            
            current=self.head
            while current.next is not None:
                current=current.next
            current.next=node
            node.prev=current
    def display(self):
        current=self.head
        while current is not None:
            print(current.data,"<->",end=" ")
            current=current.next
        print("None")        
    def delete_node(self,data):
        if self.head is None:
            print("list is empty")
            return
        if self.head.data==data:
            self.head=self.head.next
            if self.head is not None:
                self.head.prev=None
            print("deleted")
            return
        current=self.head
        while current is not None:
            if current.data==data:
                current.prev.next=current.next
                if current.next is not None:
                    current.next.prev=current.prev
                print("deleted")
                return
            current=current.next
        print("not found")
l1=DoubleLinkedList()
l1.add_node(10)
l1.add_node(20)
l1.add_node(30)
l1.add_node(40)
l1.display()
l1.delete_node(20)
l1.display()        