from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        #if nothing in storage
        if self.storage.length == 0:
            # add to the end 
            self.storage.add_to_tail(item)
            #and set current to head
            self.current = self.storage.head
        # if storage full
        elif self.storage.length == self.capacity:
            #overwrite current with new item
            self.current.value = item
            #if current is tail
            if self.current == self.storage.tail:
                #current now head
                self.current = self.storage.head
                # current is next
            else:self.current = self.current.next
            #add to the end
        else:
            self.storage.add_to_tail(item)
        

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        #setting node to head
        node= self.storage.head
       
        while node is not None:
            #add node to list buffer contents
            list_buffer_contents.append(node.value)

            #move to next
            node = node.next

        # TODO: Your code here

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
