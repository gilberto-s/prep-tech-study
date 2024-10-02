"""
Add a node to the Linked list
Delete a node from the Linked list.
Search a node in Linked list
"""


class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None


class linked_list:
    def __init__(self) -> None:
        self.head = None

    def print_list(self):
        current_node = self.head
        print("\n---------------")
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def append_node(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

    def delete_node(self, data):
        if self.head.data == data:
            self.head = self.head.next
            return

        current_node = self.head
        while current_node:
            next_node = current_node.next
            if next_node.data == data:
                current_node.next = next_node.next
                return
            current_node = current_node.next

    def search_node(self, data):
        if self.head.data == data:
            return self.head

        current_node = self.head
        while current_node:
            if current_node.data == data:
                return current_node
            current_node = current_node.next

        return None


items = linked_list()

items.append_node("g")
items.append_node("o")
items.append_node("m")
items.append_node("u")

print("initial linked list:")
items.print_list()

print("\nremove 'g':")
items.delete_node("g")
items.print_list()

print(f"\nsearch 'g' in the linked list: {items.search_node('g')}")
print(f"\nsearch 'm' in the linked list: {items.search_node('m')}")
