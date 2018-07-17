import unittest
import sys
sys.path.append('..')
import chocolatedistribution.getcuts

class TestScoreMethod(unittest.TestCase):
    """Class with the unit tests.
    """

    def test_given(self):
        chocolates = [2, 5, 7]
        children = [3, 2, 5, 1]
        cuts = chocolatedistribution.getcuts.giveChocolate(chocolates, children)
        self.assertEqual(cuts, 2)

    def test_exact(self):
        chocolates = [3, 2, 5, 1]
        children = [3, 2, 5, 1]
        cuts = chocolatedistribution.getcuts.giveChocolate(chocolates, children)
        self.assertEqual(cuts, 0)

    def test_extra_one(self):
        chocolates = [3, 2, 5, 2]
        children = [3, 2, 5, 1]
        cuts = chocolatedistribution.getcuts.giveChocolate(chocolates, children)
        self.assertEqual(cuts, 1)

    def test_extra_bigger_pieces(self):
        chocolates = [10, 8]
        children = [5, 6, 7]
        cuts = chocolatedistribution.getcuts.giveChocolate(chocolates, children)
        self.assertEqual(cuts, 2)
    
    def test_extra_smaller_pieces(self):
        chocolates = [3, 4, 4, 1, 2, 3, 1]
        children = [5, 6, 7]
        cuts = chocolatedistribution.getcuts.giveChocolate(chocolates, children)
        self.assertEqual(cuts, 0)   

if __name__ == '__main__':
    unittest.main()