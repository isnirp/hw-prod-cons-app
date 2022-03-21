import unittest
from dummy_app import BoundedQueue

class TestDummyApp(unittest.TestCase):

    def setUp(self):
        pass

    def test_add(self):
        queue_ = BoundedQueue(queue_capacity=2)
        queue_.add(name='Prince')

        self.assertEqual(queue_.len_(), 1)

    def test_take(self):
        queue_ = BoundedQueue(queue_capacity=2)
        queue_.add(name='Prince')
        result = queue_.take()

        self.assertEqual(result, "Prince")

if __name__ == '__main__':
    unittest.main()