# LinkedList: A doubly-linked list.
# Bonus: Has an insert_in_order that, when used, keeps the values of
#        each node in ascending order.
# Implement as many operations as possible with recursion.
# If you can't figure it out recursively, use a loop. (But then refactor
# your implementation into a recursive one!)
# Your implementation should pass the tests in test_sorted_list.py.
# Baleria Reyes

class LinkedList:

    def __init__(self, num=None):
        self.value = num
        self.next = self
        self.prev = self


    def fake_value(self):
        return self.value

    def is_sentinel(self):
        return self.value == None

    def is_empty(self):
        if self.prev != self or self.next != self:
            return False
        else:
            return True   

    def is_last(self):
        return self.next.is_sentinel()   
    
    def last(self):
        return self.next

    def append(self, item):
        self.next = item
        self.prev = item
        item.prev = self
        item.next = self



