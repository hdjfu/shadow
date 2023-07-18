class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self, root):
        self.root = Node(root)

    def preorder(self, start, records):
        if start is not None:
            records.append(start.value) # Root
            records = self.preorder(start.left, records) # Left subtree
            records = self.preorder(start.right, records)  # Rifht subtree
        return records
    
    def postorder(self, start, records):
        if start is not None:
            records = self.postorder(start.left, records) # Left subtree
            records = self.postorder(start.right, records)  # Rifht subtree
            records.append(start.value) # Root
        return records

# Root -> Left subtree -> Right subtree

tree = Tree(5)
tree.root.left = Node(3)
tree.root.right = Node(4)
tree.root.left.left = Node(2)
tree.root.left.right = Node(8)

print(tree.preorder(tree.root,[]))
print(tree.postorder(tree.root, []))