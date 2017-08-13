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


a = LinkedList()
print('Hi This is my linked list.')
print('_______________________________________________________')
print('I will insert 309, 30, 302, 302, 304')
a.insert_last(309)
a.insert_last(30)
a.insert_last(302)
a.insert_last(302)
a.insert_last(304)
print('After insert my linked list is')
a.print()
print('_______________________________________________________')
print('I don\'t like 30 I will delete 30')
a.delete_node(30)
print('After I delete 30 my linked list is')
a.print()
print('_______________________________________________________')
print('Now I want 30 back, but I want two in fist and last')
a.insert_first(30)
a.insert_last(30)
print('After I do my linked list is')
a.print()
print('_______________________________________________________')
print('I don\'t like 302 I will delete 302')
a.delete_node(302)
print('After I delete 302 my linked list is')
a.print()
print('_______________________________________________________')
print('Now my linked list has many item, I cannot remember that has 90 item')
a.delete_node(302)
print('Ok! my linked list can search....')
if a.search(90):
    print('Result: my linked list has 90')
else:
    print('Result: my linked list does not has 90')
print('_______________________________________________________')
print('I want to copy my linked list to another that name AAA')
AAA = LinkedList(a)
print('Now copy successful my AAA is')
AAA.print()
print('I want to add 90 to AAA, my AAA is')
AAA.insert_last(90)
AAA.print()
print('_______________________________________________________')
print('I will show my 2 list')
print('My Linked List: ')
a.print()
print('AAA: ')
AAA.print()
