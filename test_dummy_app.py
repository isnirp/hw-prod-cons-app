import unittest
from concurrent import futures
from dummy_app import BoundedQueue
import dummy_app

class TestDummyApp(unittest.TestCase):

    def setUp(self):
        self.queue_ = BoundedQueue(queue_capacity=2)

    def test_add(self):
        self.queue_.add(name='Prince')

        self.assertEqual(self.queue_.len_(), 1)

    def test_take(self):
        self.queue_.add(name='Prince')
        result = self.queue_.take()

        self.assertEqual(result, "Prince")

    def test_producer_consumer(self):
        queue_2 = BoundedQueue(queue_capacity=2)
        with futures.ThreadPoolExecutor() as executor:
            executor.submit(dummy_app.hw_producer, "Rita", queue_2)
            executor.submit(dummy_app.hw_consumer, queue_2)

if __name__ == '__main__':
    unittest.main()