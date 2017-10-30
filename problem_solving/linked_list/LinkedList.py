from Node import *

class LinkedList:

    __slots__ = ['tail', 'head']

    def __init__(self,gene=''):

        self.head = Node()
        self.tail = self.head

        for v in gene:
            self.append(v)

        return None


    def append(self, item):
        new_node = Node(item,None)

        if self.head.value == None:
            self.head = new_node
            self.tail = self.head
        else:
            if self.head.next == None:
                self.head.next = new_node

            self.tail.next = new_node
            self.tail = new_node

    def join(self, other):
        self.tail.next = other.head
        self.tail = other.tail


    def splice(self, ind, other):
        node_of_interest = self.head
        for _ in range(0,ind):
            node_of_interest = node_of_interest.next

        other.tail.next = node_of_interest.next
        node_of_interest.next = other.head


    def snip(self, l1, l2):
        """
        Snip removes everything from l1 to l2 (excluding l2)
        """
        node_of_interest = self.head
        first_node = None
        last_node = None

        if l1 >= l2:
            raise ValueError('Exception: l1 should be less than l2')

        for index in range(0,l2 + 1):

            if index == l1 - 1:
                first_node = node_of_interest
            if l2 == index:
                last_node = node_of_interest
                first_node.next = last_node

            if node_of_interest is None:
                raise ValueError('Exception: l2 exceeded the linkedlist len')

            node_of_interest = node_of_interest.next


    def search(self,repstr,find_all=False):

        old_node = current_node = self.head
        results = []

        while current_node.next is not None:
            if current_node.value == repstr[0]:
                potential_first_node = old_node
                temp_node = current_node.next
                is_found = True

                for ind in range(1,len(repstr)):

                    if temp_node.value == repstr[ind]:
                        temp_node = temp_node.next
                    else:
                        is_found = False
                        break

                if is_found:
                    results.append([potential_first_node,temp_node])
                    if not find_all:
                        return is_found, results


            old_node = current_node
            current_node = current_node.next

        if len(results) > 0:
            is_found = True
        else:
            is_found = False

        return is_found, results

    def replace(self, repstr, other):
        # find the repstr
        is_found, results = self.search(repstr)

        if is_found:
            print results
            for result in results:
                first_node = result[0]
                last_node = result[1]
                first_node.next = other.head
                other.tail.next = last_node


    def copy(self):
        copied_list = LinkedList()
        current_node = self.head

        while current_node:
            copied_list.append(current_node.value)
            current_node = current_node.next

        return copied_list

    def __str__(self):
        string_to_return = '[ '

        if self.head.next is not None:

            current_node = self.head

            while current_node:
                string_to_return += current_node.value + " "
                current_node = current_node.next

        string_to_return += ']'
        return string_to_return
