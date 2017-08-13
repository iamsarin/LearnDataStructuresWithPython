class Node:
    info = None
    nextNode = None


class LinkedList:
    count: int = 0
    current: Node = None
    first: Node = None
    last: Node = None

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

        while self.current:
            print(self.current.info, ' ', end='')
            self.current = self.current.nextNode

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
        node_to_insert_at_the_first = Node()
        node_to_insert_at_the_first.info = info

        node_to_insert_at_the_first.nextNode = self.first

        self.first = node_to_insert_at_the_first
        self.count = self.count + 1

        if self.last is None:
            self.last = node_to_insert_at_the_first

    def insert_last(self, info):
        node_to_insert_at_the_last = Node()
        node_to_insert_at_the_last.info = info

        self.count = self.count + 1

        if self.last is None:
            self.first = node_to_insert_at_the_last
            self.last = node_to_insert_at_the_last
        else:
            self.last.nextNode = node_to_insert_at_the_last
            self.last = node_to_insert_at_the_last

    def delete_node(self, info):
        node_before_running = None
        node_running = self.first

        while node_running is not None:
            if info == node_running.info:
                self.count = self.count - 1
                if node_before_running is None:
                    self.first = node_running.nextNode
                else:
                    node_before_running.nextNode = node_running.nextNode
                    if node_running.nextNode is None:
                        self.last = node_before_running
            else:
                node_before_running = node_running

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


class Stack(LinkedList):
    def push(self, info):
        self.insert_first(info)

    def pop(self):
        if self.first is None:
            return None
        info = self.first.info
        self.first = self.first.nextNode
        self.count = self.count - 1
        return info

    def print(self):
        print('-'.center(10, '-'))
        running_node = self.first
        while running_node is not None:
            print(str(running_node.info).center(10, ' '))
            running_node = running_node.nextNode
        print('-'.center(10, '-'))


print('Hello Every one. I am STACK. I can push and pop')
print('_______________________________________________________')
print('Ok, Now I will push 10, 20, 30, 40, and 50 to stack')
my_stack = Stack()
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)
my_stack.push(40)
my_stack.push(50)
print('See my stack')
my_stack.print()
print('_______________________________________________________')
print('I want to get and delete first item of stack (pop)')
print('I get ', my_stack.pop())
print('Now my stack has')
my_stack.print()
print('_______________________________________________________')
print('I want to add 100 to top (push)')
print('Now my stack has')
my_stack.push(100)
my_stack.print()
print('_______________________________________________________')

my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.pop()
