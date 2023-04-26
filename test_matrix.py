import unittest

class TestSolve(unittest.TestCase):
    
    def test_solve(self):
        matrix1 = [[0, 0, 0, 0, 0],
                   [1, 1, 1, 1, 0],
                   [0, 0, 0, 0, 0],
                   [0, 1, 1, 1, 1],
                   [0, 0, 0, 0, 0]]
        self.assertEqual(solve(matrix1), "COPS")
        
        matrix2 = [[0, 0, 0, 0, 0],
                   [1, 1, 1, 1, 0],
                   [0, 0, 0, 0, 0],
                   [1, 1, 1, 1, 1],
                   [0, 0, 0, 0, 1]]
        self.assertEqual(solve(matrix2), "ROBBERS")

if __name__ == '__main__':
    unittest.main()
