from threading import Thread, Condition
from typing import List
import logging

class BoundedQueue:
    def __init__(self, queue_capacity: int):
        """ this class tries to module a queue object by using a list"""
        self.max_size = queue_capacity
        self.queue_ = []
        self.condition_ = Condition()

        self.log = logging.getLogger("dummy-logger")


    def add(self, name: str):
        """ add name to queue"""
        self.condition_.acquire()
        try:
            while len(self.queue_) == self.max_size:
                self.condition_.wait()

            self.queue_.append(name)
            print(f'added {name}')
            # self.log.debug(f'added {name}')
            self.condition_.notify()
        finally:
            self.condition_.release()

    def take(self):
        """pop name from queue"""
        self.condition_.acquire()
        try:
            while len(self.queue_) == 0:
                self.condition_.wait()

            name = self.queue_.pop()
            self.condition_.notify()
            return name
        finally:
            self.condition_.release()

    def len_(self) -> int:
        return len(self.queue_)

def hw_producer(name: str, queue_:BoundedQueue):
    queue_.add(name)

def hw_consumer(queue_:BoundedQueue):
    name = queue_.take()
    print(f'hello {name}')

def main():
    queue_ = BoundedQueue(queue_capacity=1)
    name = "Rita"
    thread_producer = Thread(target=hw_producer, args=(name, queue_))
    thread_consumer = Thread(target=hw_consumer, args=(queue_,))

    thread_producer.start()
    thread_consumer.start()

    thread_producer.join()
    thread_consumer.join()

    print(f'goodbye {name}')

if __name__ == '__main__':
    main()