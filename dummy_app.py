from threading import Thread, Lock
from typing import List
import logging

class BoundedQueue:
    def __init__(self, queue_capacity: int):
        self.max_size = queue_capacity
        self.q = self._get_queue(capacity = queue_capacity)
        self.lock = Lock()

        self.log = logging.getLogger("dummy-logger")


    def add(self, name: str):
        # lock write access to queue
        self.lock.acquire()
        try:
            while len(self.q) == self.max_size:
                # block thread
                pass
            self.q.append(name)
            # notify item added
        finally:
            self.lock.release()

    def take(self):
        # lock read access to queue
        self.lock.acquire()
        try:
            while len(self.q) == 0:
                # block thread
                pass
            #self.q.pop(i)
            for i in range(len(self.q)):
                name = self.q[i]
                self.log.info(f'Hello %s', name)
            # motify empty
        finally:
            self.lock.release()

    def _get_queue(self, capacity: int) -> List:
        return [None]*capacity