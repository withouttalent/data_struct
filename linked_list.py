from dataclasses import dataclass
import time

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f'Node ({self.value}, {self.next.value})'


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __str__(self):
        if self.first is not None:
            current = self.first
            out = f'LinkedList [\n{str(current.value)} \n'
            while current.next is not None:
                current = current.next
                out += f'{str(current.value)}\n'
            return out + ']'
        return 'LinkedList []'

    def clear(self):
        self.__init__()

    def append(self, x):
        self.length += 1
        if self.first is None:
            self.first = self.last = Node(x, None)
        else:
            self.last.next = self.last = Node(x, None)

    def push(self, x):
        self.length += 1
        if self.first is None:
            self.first = self.last = Node(x, None)
        else:
            self.first = Node(x, self.first)

    def bubble(self):
        for i in range(self.length -1, 0, -1):
            current = self.first
            while current.next is not None:
                time.sleep(1)
                if current.value > current.next.value:
                    new = current.next #Вторая нода
                    if current.next is None:
                        current.next = None
                    else:
                        current.next = current.next.next # ссылка первой ноды ссылается на третий эл
                    new.next = current # ссылка второй ноды ссылается на первый элемент
                print(current)
                current = current.next


    def __setitem__(self, index, value):
        # При неверном индексе должен поднимать ошибку
        self.length += 1
        if self.first is None:
            self.last = self.first = Node(value, None)
            return
        if index == 0:
            self.first = Node(value, None)
            return
        curr = self.first
        count = 0
        while curr is not None:
            count += 1
            if count == index:
                curr.next = Node(value, curr.next)
                if curr.next.next is None:
                    self.last = curr.next
                break
            curr = curr.next

    def __delitem__(self, index):
        self.length -= 1
        if self.first is None:
            raise IndexError('List empty')
        if index == 0:
            self.first = self.first.next
            return
        current = self.first
        count = 0
        while current.next is not None:
            count += 1
            if count == index:
                current.next = current.next.next
            break


    def __len__(self):
        return self.length


l = LinkedList()
l.append(12)
l.append(2)
l.append(1)
l.append(4)
l[2] = 62
# l.bubble()
print(l) # Получаем 12, 2, 62, 1, 4
l.bubble()
print(l) # Должны 1, 2, 4, 12, 62
print(len(l))

#
# l = [42, 1, 32, 64, 13, 74, 42, 45]
#
#
# def bubbleSort(alist):
#     for passnum in range(len(alist)-1,0,-1):
#         for i in range(passnum):
#             if alist[i]>alist[i+1]:
#                 temp = alist[i]
#                 alist[i] = alist[i+1]
#                 alist[i+1] = temp
#
# alist = [54,26,93,17,77,31,44,55,20]
# bubbleSort(alist)
# print(alist)