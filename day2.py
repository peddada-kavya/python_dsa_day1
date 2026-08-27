class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def add_node(self,data):
        node=Node(data)
        if not self.head:
            self.head=node
        else:
            current=self.head
            #if list is not empty
            #it will iterare through the list until it reaches the last node
            # while current.next is not None:
            #     current=current.next
            # current.next=node
            while current.next is not None:
                current=current.next
            current.next=node
    def delete_node(self,data):
                #empty list
                if self.head is None:
                    print("list is empty")
                    return 
                #deleting the head node   
                if self.head.data==data:
                    self.head=self.head.next
                    print("deleted")
                    return
                #deleting the node in between or at the end
                current=self.head
                while current.next is not None:
                    if current.next.data==data:
                        current.next=current.next.next
                        print("deleted")
                        return
                    current=current.next
                print("not found")
    def display(self):
        current=self.head
        while current is not None:
            print(current.data,"->",end=" ")
            current=current.next
        print("None")
    def insert_at_beginning(self,data):
        node=Node(data)
        if not self.head:
            self.head=node
        else:
            node.next=self.head
            self.head=node
    def insert_at_kth_position(self,data,k):
        node=Node(data)
        if not self.head:
            self.head=node
        else:
            current=self.head
            count=1
            while current is not None and k>1:
                current=current.next
                count+=1
                if count==k-1:
                    node.next=current.next
                    current.next=node
                    print("inserted at kth position")
                    return
            print("Not found")    
            

ll1=Linkedlist()
ll1.add_node(10)
ll1.add_node(20)
ll1.add_node(30)
ll1.add_node(40)
ll1.display()
ll1.delete_node(30)
ll1.display()  
ll1.insert_at_beginning(5)
ll1.display()
ll1.insert_at_kth_position(25,3)
ll1.display()                 