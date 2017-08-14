class Node:
    info = None
    left = None
    right = None


class BST:
    def __init__(self):
        self.__count: int = 0
        self.__root: Node = None

    def insert(self, info):
        node_to_be_insert = Node()
        node_to_be_insert.info = info
        node_to_be_insert.left = None
        node_to_be_insert.right = None

        self.__count = self.__count + 1

        # empty tree
        if self.__root is None:
            self.__root = node_to_be_insert
            return

        # Already root node
        current = self.__root

        while current is not None:
            if info == current.info:
                break

            # info to be insert greater than current then go to right
            if info > current.info:
                if current.right is None:
                    current.right = node_to_be_insert
                    break
                else:
                    current = current.right

            # info to be insert less than current then go to left
            else:
                if current.left is None:
                    current.left = node_to_be_insert
                    break
                else:
                    current = current.left

    def search(self, info):
        current = self.__root
        while current is not None:
            if current.info == info:
                return True
            elif info > current.info:
                current = current.right
            else:
                current = current.left

        return False

    def __in_order_traverse(self, node: Node):
        if node is None:
            return

        self.__in_order_traverse(node.left)
        print(node.info, end=', ')
        self.__in_order_traverse(node.right)

    def in_order_traverse(self):
        if self.is_empty():
            return
        self.__in_order_traverse(self.__root)
        print()

    def __pre_order_traverse(self, node: Node):
        if node is None:
            return

        print(node.info, end=', ')
        self.__pre_order_traverse(node.left)
        self.__pre_order_traverse(node.right)

    def pre_order_traverse(self):
        if self.is_empty():
            return
        self.__pre_order_traverse(self.__root)
        print()

    def __post_order_traverse(self, node: Node):
        if node is None:
            return

        self.__post_order_traverse(node.left)
        self.__post_order_traverse(node.right)
        print(node.info, end=', ')

    def post_order_traverse(self):
        if self.is_empty():
            return
        self.__post_order_traverse(self.__root)
        print()

    def min(self):
        current = self.__root
        info = None
        while current is not None:
            info = current.info
            current = current.left

        return info

    def max(self):
        current = self.__root
        info = None
        while current is not None:
            info = current.info
            current = current.right

        return info

    def is_empty(self):
        return self.__count == 0


my_bst = BST()
my_bst.insert(11)
my_bst.insert(7)
my_bst.insert(15)
my_bst.insert(5)
my_bst.insert(3)
my_bst.insert(9)
my_bst.insert(8)
my_bst.insert(10)
my_bst.insert(13)
my_bst.insert(12)
my_bst.insert(14)
my_bst.insert(20)
my_bst.insert(18)
my_bst.insert(25)

print(7, my_bst.search(7))
print(15, my_bst.search(15))
print(8, my_bst.search(8))
print('InOrder: ')
my_bst.in_order_traverse()
print('PreOrder: ')
my_bst.pre_order_traverse()
print('PostOrder: ')
my_bst.post_order_traverse()

print('max', my_bst.max())
print('min', my_bst.min())
