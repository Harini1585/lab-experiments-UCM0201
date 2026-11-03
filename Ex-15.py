
# Binary Search Tree for Student Records

# Create a node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Insert a student register number
def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)

    return root


# Search for a student register number
def search(root, key):
    if root is None:
        return False

    if root.data == key:
        return True
    elif key < root.data:
        return search(root.left, key)
    else:
        return search(root.right, key)


# Display records using inorder traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# Main program
root = None

register_numbers = [50, 30, 70, 20, 40, 60, 80]

for number in register_numbers:
    root = insert(root, number)

print("Student Register Numbers:")
inorder(root)

key = 60

print("\n\nSearching for Register Number:", key)

if search(root, key):
    print("Student Record Found")
else:
    print("Student Record Not Found")
