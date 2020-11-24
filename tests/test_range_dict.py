
import unittest
from src.range_dict import RangeDict

class TestRangeDict(unittest.TestCase):

    def test_getitem(self):
        rd = RangeDict({(1,10):1, (11,20):2})

        self.assertEqual(rd[5], 1, "should return 1")
        self.assertEqual(rd[10], 1, "should return 1")
        self.assertEqual(rd[11], 2, "should return 2")

    def test_add(self):
        rd = RangeDict()
        rd[(1,10)] = 1
        self.assertEqual(rd[8], 1, "should return 1")


if __name__ == '__main__':
    unittest.main()
