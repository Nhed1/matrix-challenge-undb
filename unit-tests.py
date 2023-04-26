import unittest

from cops_and_robbers import cops_and_robbers

class TestCopsAndRobbers(unittest.TestCase):
    
    def test_cops_win(self):
        matrix = [
            [0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1],
            [1, 0, 1, 0, 1],
            [1, 1, 0, 0, 1],
            [1, 1, 1, 1, 1]
        ]
        self.assertEqual(cops_and_robbers(matrix), "COPS")
        
    def test_robbers_win(self):
        matrix = [
            [1, 0, 0, 0, 0],
            [1, 1, 0, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0]
        ]
        self.assertEqual(cops_and_robbers(matrix), "ROBBERS")
        
    def test_no_way_out(self):
        matrix = [
            [0, 1, 1, 1, 1],
            [0, 0, 0, 0, 1],
            [1, 1, 1, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1]
        ]
        self.assertEqual(cops_and_robbers(matrix), "ROBBERS")
        
    def test_cops_already_at_target(self):
        matrix = [
            [0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1],
            [1, 0, 1, 0, 1],
            [1, 1, 0, 1, 1],
            [1, 1, 1, 1, 0]
        ]
        self.assertEqual(cops_and_robbers(matrix), "COPS")
        
    def test_empty_matrix(self):
        matrix = [[]]
        with self.assertRaises(ValueError):
            cops_and_robbers(matrix)
        
    def test_invalid_matrix_size(self):
        matrix = [[0, 1, 0], [1, 0, 1]]
        with self.assertRaises(ValueError):
            cops_and_robbers(matrix)
            
    def test_invalid_matrix_values(self):
        matrix = [
            [0, 1, 2, 0, 1],
            [1, 1, 1, 1, 1],
            [1, 0, 1, 0, 1],
            [1, 1, 0, 0, 1],
            [1, 1, 1, 1, 1]
        ]
        with self.assertRaises(ValueError):
            cops_and_robbers(matrix)
