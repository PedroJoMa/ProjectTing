from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.queue = []

    def size(self):
        return len(self.queue)

    def __len__(self):
        return self.size()

    def enqueue(self, value):
        return self.queue.append(value)

    def is_empty(self):
        return self.queue == []

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)

    def search(self, index):
        length = self.size()
        if not (0 <= index < length):
            raise IndexError("Índice Inválido ou Inexistente")
        return self.queue[index]
