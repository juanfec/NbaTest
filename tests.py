import unittest
import findPairs

class TestFindPairs(unittest.TestCase):

    def testFindPairs(self):
        l = [2,2]
        solution = findPairs.FindPairs(l,len(l),4).findPairs()
        self.assertEqual([[0, 1]],solution)
    
    def testParisInTheMiddle(self):
        l = [0,1,2,3,4,4,4,4,5,6,7]
        solution = findPairs.FindPairs(l,len(l),8).findPairs()
        solution.sort()
        self.assertEqual([[1, 10],[2, 9],[3, 8],[4, 5],[4, 6],[4, 7],[5, 6],[5, 7],[6, 7]],solution)

    def testParisInTheCorners(self):
        l = [0,3,3,3,3,3,3,3,3,3,7]
        solution = findPairs.FindPairs(l,len(l),7).findPairs()
        solution.sort()
        self.assertEqual([[0, 10]],solution)

    def testNegativeNumbers(self):
        l = [-2,0,1,3,4,5,6,7]
        solution = findPairs.FindPairs(l,len(l),5).findPairs()
        solution.sort()
        self.assertEqual([[0, 7],[1, 5],[2, 4]],solution)

    def testNotPairs(self):
        l = [2,2]
        solution = findPairs.FindPairs(l,len(l),1).findPairs()
        self.assertEqual([],solution)

    def testPairsInCenterAndDiferentPlaces(self):
        l = [2,3,4,4,5,6,7,7,9,11,12]
        solution = findPairs.FindPairs(l,len(l),11).findPairs()
        solution.sort()
        self.assertEqual([[0, 8],[2, 6],[2, 7],[3, 6],[3, 7],[4, 5]],solution)

    def testAllPairs(self):
        l = [2,2,2,2,2,2]
        solution = findPairs.FindPairs(l,len(l),4).findPairs()
        solution.sort()
        self.assertEqual([[0, 1],[0, 2],[0, 3],[0, 4],[0, 5],[1, 2],[1, 3],[1, 4],[1, 5],[2, 3],[2, 4],[2, 5],[3, 4],[3, 5],[4, 5]],solution)

if __name__ == '__main__':
    unittest.main()