import unittest
from dummy_app import BoundedQueue

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

if __name__ == '__main__':
    unittest.main()