class HashTable:
    table = [None] * 37

    def put(self, key, value):
        position = self.__lose_lose_hash_cde(key)
        print(position, ' - ', key)
        self.table[position] = value

    def remove(self, key):
        self.table[self.__lose_lose_hash_cde(key)] = None

    def get(self, key):
        return self.table[self.__lose_lose_hash_cde(key)]

    @staticmethod
    def __lose_lose_hash_cde(key):
        my_hash = 0
        for i in list(key):
            my_hash += int(ord(i))

        # print('sum', my_hash)
        return my_hash % 37


hash_table = HashTable()
hash_table.put('Gandalf', 'gandalf@email.com')
hash_table.put('John', 'johnsnow@email.com')
hash_table.put('Tyrion', 'tyrion@email.com')

print("Now, let's test the get  method: ", end='')
print(hash_table.get('Gandalf'))
print(hash_table.get('Loiane'))

print("Next, let's try to remove Gandalf  from HashTable : ", end='')
hash_table.remove('Gandalf')
print(hash_table.get('Gandalf'))
