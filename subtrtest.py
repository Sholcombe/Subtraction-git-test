import unittest
import subtract


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(subtract.subtract(6,3), 3)


if __name__ == '__main__':
    unittest.main()
