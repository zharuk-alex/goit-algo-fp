class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        self._current = self.head
        return self

    def __next__(self):
        if self._current:
            data = self._current.data
            self._current = self._current.next
            return data
        else:
            raise StopIteration

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next

    # O(n**2)
    def insertion_sort(self):
        if self.head is None or self.head.next is None:
            return

        sorted_list = self.head
        to_insert = self.head.next
        sorted_list.next = None

        while to_insert:
            curr = to_insert
            to_insert = to_insert.next
            if curr.data < sorted_list.data:
                curr.next = sorted_list
                sorted_list = curr
            else:
                search = sorted_list
                while search.next is not None and curr.data > search.next.data:
                    search = search.next
                curr.next = search.next
                search.next = curr

        self.head = sorted_list

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        self.head = prev


def merge_llists(ll1, ll2):
    def iter_ll(head1, head2):
        if head1 is None:
            return head2
        if head2 is None:
            return head1

        if head1.data < head2.data:
            head1.next = iter_ll(head1.next, head2)
            return head1
        else:
            head2.next = iter_ll(head2.next, head1)
            return head2

    new_ll = LinkedList()
    new_ll.head = iter_ll(ll1.head, ll2.head)

    return new_ll


if __name__ == "__main__":
    ll_first = LinkedList()
    ll_second = LinkedList()

    ll_second.insert_at_beginning(33)
    ll_second.insert_at_beginning(66)
    ll_second.insert_at_beginning(12)
    # Вставляємо вузли в початок
    ll_first.insert_at_beginning(17)
    ll_first.insert_at_beginning(8)
    ll_first.insert_at_beginning(10)
    ll_first.insert_at_beginning(15)

    # Вставляємо вузли в кінець
    ll_first.insert_at_end(20)
    ll_first.insert_at_end(25)

    # Друк зв'язного списку
    print("Зв'язний список:")

    # sort
    ll_first.insertion_sort()
    print("sorted")
    ll_first.print_list()

    # reverse
    ll_first.reverse()
    print("reversed")
    ll_first.print_list()

    # have to be sorted before concate
    ll_first.insertion_sort()
    ll_second.insertion_sort()
    ll3 = merge_llists(ll_first, ll_second)
    print("merged")
    ll3.print_list()
