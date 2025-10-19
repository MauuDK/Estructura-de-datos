
class Order:
    def __init__(self, qtty, customer):
        self.customer = customer
        self.qtty = qtty

    def print(self):
        print(f"     Customer: {self.customer}")
        print(f"     Quantity: {self.qtty}")
        print("     ------------")

    def get_qtty(self):
        return self.qtty

    def get_customer(self):
        return self.customer


class Node:
    def __init__(self, info):
        self.info = info
        self.next = None


class LinkedQueue:
    def __init__(self):
        self.top = None
        self.tail = None
        self.count = 0

    def size(self):
        return self.count

    def is_empty(self):
        return self.count == 0

    def front(self):
        if self.is_empty():
            return None
        return self.top.info

    def enqueue(self, info):
        new_node = Node(info)
        if self.is_empty():
            self.top = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            return None
        info = self.top.info
        self.top = self.top.next
        self.count -= 1
        if self.top is None:
            self.tail = None
        return info

    def print_info(self):
        print("********* QUEUE DUMP *********")
        print(f"Size: {self.count}")
        node = self.top
        i = 1
        while node:
            print(f"** Element {i}")
            node.info.print()
            node = node.next
            i += 1
        print("******************************")

    def get_nth(self, pos):
        if pos < 1 or pos > self.count:
            return None
        node = self.top
        for _ in range(1, pos):
            node = node.next
        return node.info


if __name__ == "__main__":
    queue = LinkedQueue()

    order1 = Order(20, "cust1")
    order2 = Order(30, "cust2")
    order3 = Order(40, "cust3")
    order4 = Order(50, "cust4")

    queue.enqueue(order1)
    queue.print_info()

    queue.enqueue(order2)
    queue.print_info()

    queue.enqueue(order3)
    queue.print_info()

    queue.enqueue(order4)
    queue.print_info()

    print("Front element:")
    queue.front().print()

    print("Dequeue element:")
    queue.dequeue().print()
    queue.print_info()

    print("3rd element in queue:")
    queue.get_nth(3).print()