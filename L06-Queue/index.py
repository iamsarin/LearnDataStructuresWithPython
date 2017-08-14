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

    def print(self):
        print('| ', end='')
        running_node = self.first
        while running_node is not None:
            print(running_node.info, ', ', end='')
            running_node = running_node.nextNode
        print('|')


print('Hello Every one. I am Queue. I can enqueue and dequeue')
print('_______________________________________________________')
print('Ok, Now I will add 10, 20, 30, 40, and 50 to queue')
my_stack = Queue()
my_stack.enqueue(10)
my_stack.enqueue(20)
my_stack.enqueue(30)
my_stack.enqueue(40)
my_stack.enqueue(50)
print('See my stack')
my_stack.print()
print('_______________________________________________________')
print('I want to get and delete first item that enter to queue (dequeue)')
print('I get ', my_stack.dequeue())
print('Now my stack has')
my_stack.print()
print('_______________________________________________________')
print('I want to add 100 to queue (enqueue)')
print('Now my stack has')
my_stack.enqueue(100)
my_stack.print()
print('_______________________________________________________')
print('I will dequeue 10 times')

for i in range(0, 10):
    my_stack.dequeue()
    my_stack.print()
print('_______________________________________________________')
