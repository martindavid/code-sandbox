from Queue.Queue import Queue

if __name__ == '__main__':
    q = Queue()
    q.en_queue("first")
    print(q.queue_front())
    print(q.queue_rear())
    q.en_queue("second")
    print(q.queue_front())
    print(q.queue_rear())
    q.en_queue("third")
    print(q.queue_front())
    print(q.queue_rear())