# Queue is a FIFO queue
class Queue:
    def __init__(self, name):
        self.name = name
        self.contents = []

    # allows += to work for Queue
    def __iadd__(self, other):
        self.enqueue(other)
        return self

    def __str__(self):
        s = "Contents: "
        for item in self.contents:
            s += str(item) + ' '
        return s

    # remove from the queue
    def dequeue(self):
        return self.contents.pop(0)

    # add to the queue
    def enqueue(self, num):
        self.contents.append(num)

    def is_empty(self):
        return len(self.contents) == 0

# -----------------------------------------------------

def main():
    numbers = Queue("Numbers")

    print("Enqueue 1, 2, 3, 4, 5")
    print("---------------------")
    for number in range(1, 6):
        numbers.enqueue(number)
        print(numbers)

    print("\nDequeue one item")
    print("----------------")
    numbers.dequeue()
    print(numbers)

    print("\nDeque all items")
    print("---------------")
    while not numbers.is_empty():
        print("Item dequeued:", numbers.dequeue())
        print(numbers)

    # Enqueue 10, 11, 12, 13, 14
    for number in range(10, 15):
        numbers.enqueue(number)

    # Enqueue 15
    numbers += 15

    print("\n10, 11, 12, 13, 14, 15 enqueued")
    print("-------------------------------")
    print(numbers)

# -----------------------------------------------------

main()
