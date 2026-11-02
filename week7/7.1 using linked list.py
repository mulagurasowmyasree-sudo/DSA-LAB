class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTreeLinked:

    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            print(value, "inserted as root")
            return

        # Level order traversal to find the first empty left or right child spot
        queue = [self.root]
        while queue:
            current = queue.pop(0)

            if current.left is None:
                current.left = new_node
                print(value, "inserted to the left of", current.data)
                return
            else:
                queue.append(current.left)

            if current.right is None:
                current.right = new_node
                print(value, "inserted to the right of", current.data)
                return
            else:
                queue.append(current.right)

    def search(self, value):
        if self.root is None:
            print("Tree is empty")
            return False

        queue = [self.root]
        while queue:
            current = queue.pop(0)
            if current.data == value:
                print(value, "found in the tree")
                return True

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        print(value, "not found")
        return False

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)


# Example usage:
bt = BinaryTreeLinked()
bt.insert(10)
bt.insert(20)
bt.insert(30)
bt.insert(40)

print("\nInorder traversal:")
bt.inorder(bt.root)

print("\nPreorder traversal:")
bt.preorder(bt.root)
