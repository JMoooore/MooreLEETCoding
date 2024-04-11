import math

# parent = floor ( (idx - 1) / 2)
# leftChild = idx * 2 + 1
# rightChild = idx * 2 + 2

#   0
#  1 2
#3 4 5 6

class PriorityQueue:
    def __init__(self):
        self.items = []

    def size(self) -> int:
        return len(self.items)

    def is_empty(self):
        return self.size() == 0

    def peek(self):
        return self.items[0]

    def push(self, item):
        self.items.append(item)
        self.__sort__()

    def pop(self):
        if self.isEmpty():
            return None
        self.items[0], self.items[-1] = self.items[-1], self.items[0]
        max_item = self.items.pop()
        self.__sort__()
        return max_item

    def __sort__(self):
        i = len(self.items) - 1
        j = math.floor((i - 1) / 2)

        while j >= 0:
            if self.items[j] < self.items[i]:
                self.items[i], self.items[j] = self.items[j], self.items[i]
                i = j
                j = math.floor((i - 1) / 2)
            else:
                break


if __name__ == '__main__':
    cat = PriorityQueue()
    cat.push(1)
    cat.push(2)
    cat.push(3)
    cat.push(4)
    cat.push(5)
    cat.push(6)
    print(cat.peek())