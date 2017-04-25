class Queue(object):
    def __init__(self, limit = 5):
        self.que = []
        self.limit = limit
        self.front = None
        self.rear = None
        self.size = 0
    
    def get_que(self):
        return self.que

    def is_empty(self):
        return self.size <= 0

    def en_queue(self, item):
        if self.size >= self.limit:
            print('Queue Overflow')
            return
        else:
            self.que.append(item)

        if self.front is None:
            self.front = self.rear = 0
        else:
            self.rear = self.size

        self.size += 1

    def de_queue(self):
        if self.rear is None:
            print('Queue is empty')
            return
        else:
            self.size -= 1
            if self.size == 0:
                self.front = self.rear = None
            else:
                self.rear = self.size - 1
        return self.que.pop(0)

    def queue_rear(self):
        if self.rear is None:
            print('Queue is empty')
            return
        return self.que[self.rear]

    def queue_front(self):
        if self.front is None:
            print('Queue is empty')
            return
        return self.que[self.front]
