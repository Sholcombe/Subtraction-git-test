import unittest
import subtract


class MyTestCase(unittest.TestCase):
    def test_input(self):
        with self.assertRaises(TypeError):
            subtract('a'-3)  # add assertion here


if __name__ == '__main__':
    unittest.main()
