# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        # => check if the storage is not empty
        #       => if there is something -> loop thru node and check if key exist
        #               => if key already exist -> replace value
        #               => if not exist -> add LinkedPair
        #       => if there nothing -> add LinkedPair


        index = self._hash_mod(key)
        pair = LinkedPair(key, value)
        if self.storage[index] is not None:
            node = self.storage[index]
            while node != None:
                if node.key == key:
                    node.value = value
                    break
                elif node.next == None:
                    node.next = pair
                    break
                node = node.next
            # print("===Pair=== ", pair.key, pair.value)
        else:
            self.storage[index] = pair
            return self.storage[index].value

        return

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        if self.storage[index] is not None:
            if self.storage[index].key == key:
                self.storage[index] = None
        else:
            print(f"Warning key ({key}) not found.")
            return None
        return

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)

        if self.storage[index] == None:
            return None
        else:
            node = self.storage[index]
            while node is not None:
                if node.key == key:
                    return node.value
                else:
                    node = node.next
  


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        old_storage = self.storage
        self.capacity *= 2
        new_storage = [None] * self.capacity
        self.storage = new_storage

        for i in range(len(old_storage)):
            if old_storage[i]:
                current_node = old_storage[i]

                while current_node:
                    self.insert(current_node.key, current_node.value)
                    current_node = current_node.next

        self.storage = new_storage






if __name__ == "__main__":
    # ht1 = HashTable(4)

    # ht1.insert("key1", "test1")
    # ht1.insert("key22", "test222")
    
    # # ht1.resize()
    
    # ht1.insert("key23", "test777")
    # # ht1.remove("key1")

    # print(ht1.storage)
    ht = HashTable(8)

    ht.insert("key-0", "val-0")
    ht.insert("key-1", "val-1")
    ht.insert("key-2", "val-2")
    ht.insert("key-3", "val-3")
    ht.insert("key-4", "val-4")
    ht.insert("key-5", "val-5")
    ht.insert("key-6", "val-6")
    ht.insert("key-7", "val-7")
    ht.insert("key-8", "val-8")
    ht.insert("key-9", "val-9")

    ht.resize()


    print(f"Resize: {len(ht.storage)}")

    print(f'Retrieve 0: {ht.retrieve("key-0")}')
    print(f'Retrieve 5: {ht.retrieve("key-5")}')
    print(f'Retrieve 9: {ht.retrieve("key-9")}')




    # ht = HashTable(2)

    # ht.insert("line_1", "Tiny hash table")
    # ht.insert("line_2", "Filled beyond capacity")
    # ht.insert("line_3", "Linked list saves the day!")

    # print("")

    # # Test storing beyond capacity
    # print(ht.retrieve("line_1"))
    # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))

    # # # Test resizing
    # old_capacity = len(ht.storage)
    # ht.resize()
    # new_capacity = len(ht.storage)

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    # print(ht.retrieve("line_1"))
    # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))

    # # print("")
