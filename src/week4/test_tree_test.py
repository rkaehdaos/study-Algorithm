import unittest

import test_tree as tree


class TreeTest(unittest.TestCase):

    def test_nullHead(self):
        self.assertRaisesRegex(TypeError, 'node타입이 아닙니다')


if __name__ == '__main__':
    unittest.main()
