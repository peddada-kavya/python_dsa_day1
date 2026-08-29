#circular Linked List
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class CircularLinkedlist:
#     def __init__(self):
#         self.head=None
#     def add_node(self,data):
#         node=Node(data)
#         if not self.head:
#             self.head=node
#             node.next=self.head
#         else:
#             current=self.head
#             #if list is not empty
#             #it will iterare through the list until it reaches the last node
#             while current.next!=self.head:
#                 current=current.next
#             current.next=node
#             node.next=self.head
#     def display(self):
#         if not self.head:
#             print("list is empty")
#             return
#         current=self.head
#         while True:
#             print(current.data,"->",end=" ")
#             current=current.next
#             if current==self.head:
#                 print("self.head",self.head.data)
#                 break
#     def delete_node(self,data):
#         #empty list
#         if self.head is None:
#             print("list is empty")
#             return
#         #deleting the head node
#         if self.head.data==data:
#             if self.head.next==self.head:
#                 self.head=None
#             else:
#                 current=self.head
#                 while current.next!=self.head:
#                     current=current.next    
#                 self.head=self.head.next
#                 current.next=self.head
#             print("deleted")
#             return
#         current=self.head
#         while current.next!=self.head:
#             if current.next.data==data:
#                 current.next=current.next.next
#                 print("deleted")
#                 return
#             current=current.next
#         print("not found")               
# ll1=CircularLinkedlist()
# ll1.add_node(10)
# ll1.add_node(20)
# ll1.add_node(30)
# ll1.add_node(40)
# ll1.display()  
# ll1.delete_node(20)
# ll1.display()  
#Trees
# from platform import node


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.children = []

# class Tree:
#     def __init__(self):
#         self.root = None

#     def add_node(self, data, parent_data=None):
#         new_node = Node(data)
#         if not self.root:
#             self.root = new_node
#             return

#         if parent_data is not None:
#             # Find the parent node using the helper method
#             parent_node = self._find_node(parent_data, self.root)
#             if parent_node:
#                 parent_node.children.append(new_node)
#     # Renamed from findParent to _find_node and modified to find any node by data
#     def _find_node(self, data, node):
#         if node is None:
#             return None
#         if node.data == data:
#             return node
#         for child in node.children:
#             found_node = self._find_node(data, child)
#             if found_node:
#                 return found_node
#         return None

#     def display(self, node=None, depth=0):
#         if node is None:
#             node = self.root
#         if node is None: # Handle case of an empty tree
#             return
#         current_node = node
#         print("-" * depth + str(current_node.data))
#         for child in current_node.children:
#             self.display(child, depth + 1)

# # Instance creation and method calls should be outside the class definition
# t1 = Tree()
# t1.add_node(1)
# t1.add_node(2, 1)
# t1.add_node(3, 1)
# t1.add_node(4, 2)
# t1.add_node(5, 2)
# t1.display()

#Binary Tree
# class BinaryNode:
#     def __init__(self, data):
#         self.data=data
#         self.left=None
#         self.right=None
# class BinaryTree:
#     def __init__(self):
#         self.root=None
#     def addNode(self,data, parent_data=None):    
#         new_node=BinaryNode(data)
#         if not self.root:
#             self.root=new_node
#             return
#         self.recursiveAdd(new_node,self.root)
#     def recursiveAdd(self,node,current_node): 
#         if current_node.left is None:
#             current_node.left=node
#         elif current_node.right is None:
#             current_node.right=node
#         else:
#             self.recursiveAdd(node,current_node.left)
#     def display(self, node=None, depth=0):
#             if node is None:
#                 node = self.root
#             current_node = node
#             print("-" * depth + str(current_node.data))
#             if node.left is not None:
#                 self.display(node.left, depth + 1)
#             if node.right is not None:
#                 self.display(node.right, depth + 1)    
    
# t2=BinaryTree()
# t2.addNode(1)
# t2.addNode(2, 1)
# t2.addNode(3, 1)
# t2.addNode(4, 2)
# t2.addNode(5, 2)
# t2.display()
                          
#Binary Search Tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add_node(self, data):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
            return

        self.recursive_add(new_node, self.root)

    def recursive_add(self, node, current_node):
        if node.data < current_node.data:
            if current_node.left is None:
                current_node.left = node
            else:
                self.recursive_add(node, current_node.left)
        else:
            if current_node.right is None:
                current_node.right = node
            else:
                self.recursive_add(node, current_node.right)

    def display(self, node=None, depth=0):
        if node is None:
            node = self.root

        if node is None:
            print("Tree is empty")
            return

        print("-" * depth + str(node.data))

        if node.left is not None:
            self.display(node.left, depth + 1)

        if node.right is not None:
            self.display(node.right, depth + 1)

    def find_minimum(self, node):
        if node is None:
            return None

        while node.left is not None:
            node = node.left

        return node.data

    def find_maximum(self, node):
        if node is None:
            return None

        while node.right is not None:
            node = node.right

        return node.data

    def inorder_traversal(self, node):
        if node is not None:
            self.inorder_traversal(node.left)
            print(node.data, end=" ")
            self.inorder_traversal(node.right)

    def preorder_traversal(self, node):
        if node is not None:
            print(node.data, end=" ")
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    def postorder_traversal(self, node):
        if node is not None:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.data, end=" ")

    def remove(self, node, data):
        if node is None:
            return None

        if data < node.data:
            node.left = self.remove(node.left, data)

        elif data > node.data:
            node.right = self.remove(node.right, data)

        else:
            # Case 1: No children
            if node.left is None and node.right is None:
                return None

            # Case 2: Only right child
            elif node.left is None:
                return node.right

            # Case 3: Only left child
            elif node.right is None:
                return node.left

            # Case 4: Two children
            else:
                min_value = self.find_minimum(node.right)
                node.data = min_value
                node.right = self.remove(node.right, min_value)

        return node


# Create BST
t3 = BinarySearchTree()

# Add nodes
t3.add_node(10)
t3.add_node(5)
t3.add_node(15)
t3.add_node(3)
t3.add_node(7)

# Display BST
print("Binary Search Tree:")
t3.display()

# Minimum and Maximum
print("\nMinimum value in the BST:", t3.find_minimum(t3.root))
print("Maximum value in the BST:", t3.find_maximum(t3.root))

# Inorder Traversal
print("\nInorder Traversal:", end=" ")
t3.inorder_traversal(t3.root)

# Preorder Traversal
print("\nPreorder Traversal:", end=" ")
t3.preorder_traversal(t3.root)

# Postorder Traversal
print("\nPostorder Traversal:", end=" ")
t3.postorder_traversal(t3.root)

# Remove node
print("\n\nRemoving node with value 5...")
t3.root = t3.remove(t3.root, 5)

# Display after removal
print("\nBinary Search Tree after removing 5:")
t3.display()

# Inorder after removal
print("\nInorder Traversal after removal:", end=" ")
t3.inorder_traversal(t3.root)

print()

#circular Linked List
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class CircularLinkedlist:
#     def __init__(self):
#         self.head=None
#     def add_node(self,data):
#         node=Node(data)
#         if not self.head:
#             self.head=node
#             node.next=self.head
#         else:
#             current=self.head
#             #if list is not empty
#             #it will iterare through the list until it reaches the last node
#             while current.next!=self.head:
#                 current=current.next
#             current.next=node
#             node.next=self.head
#     def display(self):
#         if not self.head:
#             print("list is empty")
#             return
#         current=self.head
#         while True:
#             print(current.data,"->",end=" ")
#             current=current.next
#             if current==self.head:
#                 print("self.head",self.head.data)
#                 break
#     def delete_node(self,data):
#         #empty list
#         if self.head is None:
#             print("list is empty")
#             return
#         #deleting the head node
#         if self.head.data==data:
#             if self.head.next==self.head:
#                 self.head=None
#             else:
#                 current=self.head
#                 while current.next!=self.head:
#                     current=current.next    
#                 self.head=self.head.next
#                 current.next=self.head
#             print("deleted")
#             return
#         current=self.head
#         while current.next!=self.head:
#             if current.next.data==data:
#                 current.next=current.next.next
#                 print("deleted")
#                 return
#             current=current.next
#         print("not found")               
# ll1=CircularLinkedlist()
# ll1.add_node(10)
# ll1.add_node(20)
# ll1.add_node(30)
# ll1.add_node(40)
# ll1.display()  
# ll1.delete_node(20)
# ll1.display()  
#Trees
# from platform import node


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.children = []

# class Tree:
#     def __init__(self):
#         self.root = None

#     def add_node(self, data, parent_data=None):
#         new_node = Node(data)
#         if not self.root:
#             self.root = new_node
#             return

#         if parent_data is not None:
#             # Find the parent node using the helper method
#             parent_node = self._find_node(parent_data, self.root)
#             if parent_node:
#                 parent_node.children.append(new_node)
#     # Renamed from findParent to _find_node and modified to find any node by data
#     def _find_node(self, data, node):
#         if node is None:
#             return None
#         if node.data == data:
#             return node
#         for child in node.children:
#             found_node = self._find_node(data, child)
#             if found_node:
#                 return found_node
#         return None

#     def display(self, node=None, depth=0):
#         if node is None:
#             node = self.root
#         if node is None: # Handle case of an empty tree
#             return
#         current_node = node
#         print("-" * depth + str(current_node.data))
#         for child in current_node.children:
#             self.display(child, depth + 1)

# # Instance creation and method calls should be outside the class definition
# t1 = Tree()
# t1.add_node(1)
# t1.add_node(2, 1)
# t1.add_node(3, 1)
# t1.add_node(4, 2)
# t1.add_node(5, 2)
# t1.display()

#Binary Tree
# class BinaryNode:
#     def __init__(self, data):
#         self.data=data
#         self.left=None
#         self.right=None
# class BinaryTree:
#     def __init__(self):
#         self.root=None
#     def addNode(self,data, parent_data=None):    
#         new_node=BinaryNode(data)
#         if not self.root:
#             self.root=new_node
#             return
#         self.recursiveAdd(new_node,self.root)
#     def recursiveAdd(self,node,current_node): 
#         if current_node.left is None:
#             current_node.left=node
#         elif current_node.right is None:
#             current_node.right=node
#         else:
#             self.recursiveAdd(node,current_node.left)
#     def display(self, node=None, depth=0):
#             if node is None:
#                 node = self.root
#             current_node = node
#             print("-" * depth + str(current_node.data))
#             if node.left is not None:
#                 self.display(node.left, depth + 1)
#             if node.right is not None:
#                 self.display(node.right, depth + 1)    
    
# t2=BinaryTree()
# t2.addNode(1)
# t2.addNode(2, 1)
# t2.addNode(3, 1)
# t2.addNode(4, 2)
# t2.addNode(5, 2)
# t2.display()
                          
#Binary Search Tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add_node(self, data):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
            return

        self.recursive_add(new_node, self.root)

    def recursive_add(self, node, current_node):
        if node.data < current_node.data:
            if current_node.left is None:
                current_node.left = node
            else:
                self.recursive_add(node, current_node.left)
        else:
            if current_node.right is None:
                current_node.right = node
            else:
                self.recursive_add(node, current_node.right)

    def display(self, node=None, depth=0):
        if node is None:
            node = self.root

        if node is None:
            print("Tree is empty")
            return

        print("-" * depth + str(node.data))

        if node.left is not None:
            self.display(node.left, depth + 1)

        if node.right is not None:
            self.display(node.right, depth + 1)

    def find_minimum(self, node):
        if node is None:
            return None

        while node.left is not None:
            node = node.left

        return node.data

    def find_maximum(self, node):
        if node is None:
            return None

        while node.right is not None:
            node = node.right

        return node.data

    def inorder_traversal(self, node):
        if node is not None:
            self.inorder_traversal(node.left)
            print(node.data, end=" ")
            self.inorder_traversal(node.right)

    def preorder_traversal(self, node):
        if node is not None:
            print(node.data, end=" ")
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    def postorder_traversal(self, node):
        if node is not None:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.data, end=" ")

    def remove(self, node, data):
        if node is None:
            return None

        if data < node.data:
            node.left = self.remove(node.left, data)

        elif data > node.data:
            node.right = self.remove(node.right, data)

        else:
            # Case 1: No children
            if node.left is None and node.right is None:
                return None

            # Case 2: Only right child
            elif node.left is None:
                return node.right

            # Case 3: Only left child
            elif node.right is None:
                return node.left

            # Case 4: Two children
            else:
                min_value = self.find_minimum(node.right)
                node.data = min_value
                node.right = self.remove(node.right, min_value)

        return node


# Create BST
t3 = BinarySearchTree()

# Add nodes
t3.add_node(10)
t3.add_node(5)
t3.add_node(15)
t3.add_node(3)
t3.add_node(7)

# Display BST
print("Binary Search Tree:")
t3.display()

# Minimum and Maximum
print("\nMinimum value in the BST:", t3.find_minimum(t3.root))
print("Maximum value in the BST:", t3.find_maximum(t3.root))

# Inorder Traversal
print("\nInorder Traversal:", end=" ")
t3.inorder_traversal(t3.root)

# Preorder Traversal
print("\nPreorder Traversal:", end=" ")
t3.preorder_traversal(t3.root)

# Postorder Traversal
print("\nPostorder Traversal:", end=" ")
t3.postorder_traversal(t3.root)

# Remove node
print("\n\nRemoving node with value 5...")
t3.root = t3.remove(t3.root, 5)

# Display after removal
print("\nBinary Search Tree after removing 5:")
t3.display()

# Inorder after removal
print("\nInorder Traversal after removal:", end=" ")
t3.inorder_traversal(t3.root)

print()
