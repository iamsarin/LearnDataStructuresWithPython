class DoublyNode:
    info = None
    nextNode = None
    previousNode = None


class DoublyLinkedList:
    count: int = 0
    current: DoublyNode = None
    first: DoublyNode = None
    last: DoublyNode = None

    def __init__(self, node=None):
        self.count = 0
        self.current = None
        self.first = None
        self.last = None
        if node is not None:
            self.copy(node)

    def initialize_list(self):
        self.destroy_list()

    def is_empty_list(self):
        return self.count <= 0

    def print(self):
        if self.count == 0:
            return

        self.current = self.first

        while self.current is not None:
            print(self.current.info, ' ', end='')
            self.current = self.current.nextNode

        self.current = None
        print()

    def print_reverse(self):
        if self.count == 0:
            return

        self.current = self.last

        while self.current is not None:
            print(self.current.info, ' ', end='')
            self.current = self.current.previousNode

        self.current = None
        print()

    def length(self):
        return self.count

    def destroy_list(self):
        self.current = self.first
        while self.current is not None:
            temp_node = self.current
            self.current = self.current.nextNode
            del temp_node

        self.first = None
        self.last = None
        self.current = None
        self.count = 0

    def front(self):
        if self.count <= 0:
            raise Exception('Linked List is empty')
        return self.first.info

    def back(self):
        if self.count <= 0:
            raise Exception('Linked List is empty')
        return self.last.info

    def search(self, info) -> bool:
        if self.count == 0:
            return False

        self.current = self.first

        while self.current is not None:
            if self.current.info == info:
                return True
            self.current = self.current.nextNode

        self.current = None
        return False

    def insert_first(self, info):
        node_to_insert_at_the_first = DoublyNode()
        node_to_insert_at_the_first.info = info

        node_to_insert_at_the_first.nextNode = self.first
        self.first.previousNode = node_to_insert_at_the_first

        self.first = node_to_insert_at_the_first
        self.count = self.count + 1

        if self.last is None:
            self.last = node_to_insert_at_the_first

    def insert_last(self, info):
        node_to_insert_at_the_last = DoublyNode()
        node_to_insert_at_the_last.info = info

        self.count = self.count + 1

        if self.last is None:
            self.first = node_to_insert_at_the_last
            self.last = node_to_insert_at_the_last
        else:
            self.last.nextNode = node_to_insert_at_the_last
            node_to_insert_at_the_last.previousNode = self.last
            self.last = node_to_insert_at_the_last

    def delete_node(self, info):
        node_running = self.first

        while node_running is not None:
            if info == node_running.info:
                self.count = self.count - 1
                if node_running.previousNode is None:
                    node_running.previousNode = None
                    self.first = node_running.nextNode

                else:
                    node_running.previousNode.nextNode = node_running.nextNode

                    if node_running.nextNode is None:
                        self.last = node_running.previousNode
                    else:
                        node_running.nextNode.previousNode = node_running.previousNode

            node_running = node_running.nextNode

    def copy(self, linked_list=None):
        if self.first is not None:
            self.destroy_list()

        if linked_list.first is None:
            self.first = None
            self.last = None
            self.count = 0
            return

        self.current = linked_list.first
        while self.current is not None:
            self.insert_last(self.current.info)
            self.current = self.current.nextNode


class Queue(DoublyLinkedList):
    def enqueue(self, info):
        self.insert_last(info)

    def dequeue(self):
        if self.first is None:
            return None

        self.count = self.count - 1
        info = self.first.info
        self.first = self.first.nextNode
        if self.first is not None:
            self.first.previousNode = None
        return info

    def is_empty(self):
        return self.count == 0

    def print(self):
        print('| ', end='')
        running_node = self.first
        while running_node is not None:
            print(running_node.info, ', ', end='')
            running_node = running_node.nextNode
        print('|')

    def front(self):
        if self.first is None:
            return None
        return self.first.info


class Node:
    info = None
    left = None
    right = None


class BST:
    def __init__(self):
        self.__root = None
        self.__count = 0

    def is_empty(self):
        return self.__count == 0

    def insert(self, info):
        node_to_be_inset = Node()
        node_to_be_inset.info = info
        if self.__count == 0:
            self.__count = self.__count + 1
            self.__root = node_to_be_inset
            return

        self.__count = self.__count + 1;

        current = self.__root
        while True:
            if info == current.info:
                return
            elif info > current.info:
                if current.right is None:
                    current.right = node_to_be_inset
                    return
                current = current.right
            else:
                if current.left is None:
                    current.left = node_to_be_inset
                    return
                current = current.left

    def delete(self, info):
        if self.__root is None:
            return

        if self.__root.info == info:
            self.__root = None

        parent_of_current = None
        current = self.__root
        while current is not None:
            if info == current.info:
                # case current is no child
                if current.left is None and current.right is None:
                    if parent_of_current.left.info == current.info:
                        parent_of_current.left = None
                    elif parent_of_current.right.info == current.info:
                        parent_of_current.right = None
                    return
                # case current is left child
                elif current.left is None:
                    if parent_of_current.left.info == current.info:
                        parent_of_current.left = current.right
                    elif parent_of_current.right.info == current.info:
                        parent_of_current.right = current.right
                # case current is right child
                elif current.right is None:
                    if parent_of_current.left.info == current.info:
                        parent_of_current.left = current.left
                    elif parent_of_current.right.info == current.info:
                        parent_of_current.right = current.right
                # Have a child => find node that greater than info but fewest
                finding_node = current.right
                des_info = finding_node.info
                parent_finding_node = parent_of_current
                while finding_node is not None:
                    des_info = finding_node.info
                    parent_finding_node = finding_node
                    finding_node = finding_node.left

                parent_finding_node.left = None
                current.info = des_info

            parent_of_current = current
            if info > current.info:
                current = current.right
                continue
            else:
                current = current.left
                continue

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

    def bft(self):
        if self.__root is None:
            return

        my_queue = Queue()
        my_queue.enqueue(self.__root)

        while not my_queue.is_empty():
            current = my_queue.front()
            print(current.info, end=', ')

            if current.left is not None:
                my_queue.enqueue(current.left)

            if current.right is not None:
                my_queue.enqueue(current.right)

            my_queue.dequeue()


my = BST()
my.insert('F')
my.insert('D')
my.insert('B')
my.insert('A')
my.insert('C')
my.insert('E')
my.insert('J')
my.insert('G')
my.insert('K')
my.insert('I')
my.insert('H')

my.in_order_traverse()

my.bft()
