class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Spisok_one:
    def __init__(self, head=None):
        self.head = head

    def add_items(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def reverse_items(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def print_items(self):
        curr_node = self.head
        string = ""
        while curr_node:
            string = string + " " + str(curr_node.data)
            curr_node = curr_node.next
        print(string)


spisok = Spisok_one()
len_spisok = 5
for i in range(len_spisok):
    print(f'Введите {i + 1} элемент списка: ')
    spisok.add_items(int(input()))
print('Исходный список: ')
spisok.print_items()
spisok.reverse_items()
print('Список в обратном порядке: ')
spisok.print_items()
