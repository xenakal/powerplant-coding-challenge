import unittest
import numpy as np
import logging

from simplex import *


class OptimisationEngineTests(unittest.TestCase):

    def setUp(self): 
        # self.A = np.array([[15, 20, 25, 1, 0, 0, 0], 
        #                    [35, 60, 60, 0, 1, 0, 0], 
        #                    [20, 30, 25, 0, 0, 1, 0], 
        #                    [0, 250, 0, 0, 0, 0, 1]])
        # self.A = np.array([[15, 20, 25, 1, 0, 0, 0], 
        #                    [35, 60, -60, 0, 1, 0, 0], 
        #                    [20, 30, 25, 0, 0, 1, 0], 
        #                    [0, 250, 0, 0, 0, 0, 1]])
        # self.b =  np.array([1200, 3000, 1500, 500])
        # self.c =  np.array([300, 250, 450, 0, 0, 0, 0])
        pass


    def tearDown(self):
        pass

    def test_init_pivot_table(self):
        pass
        # actual_table = create_simplex_pivot_table(self.c, self.A, self.b)
        # expected_table = np.array([[15, 20, 25, 1, 0, 0, 0, 1200], [35, 60, 60, 0, 1, 0, 0, 3000], [20, 30, 25, 0, 0, 1, 0, 1500], [0, 250, 0, 0, 0, 0, 1, 500], [300, 250, 450, 0, 0, 0, 0, 0]])
        # np.testing.assert_array_almost_equal(actual_table, expected_table,decimal=3)

    def test_solver_simple_instance(self): 
        self.A = np.array([[2,1,1,0,0],
                           [2,3,0,1,0],
                           [3,1,0,0,1]])
        self.b =  np.array([18,42,24])
        self.c =  np.array([3,2,0,0,3])
        actual_powerplant_outputs, actual_total_cost = optimise_simplex(self.A, self.b, self.c)
        expected_total_cost = 33
        expected_powerplant_outputs = np.array([3, 12, 0, 0, 0])
        self.assertEqual(expected_total_cost, actual_total_cost)
        np.testing.assert_array_equal(expected_powerplant_outputs, actual_powerplant_outputs)

    def test_exists_better_solution_true(self):
        pass

    def test_exists_better_solution_false(self):
        pass

    def test_exists_better_solution_true1(self):
        pass

    def test_get_pivot_index(self):
        pass

    def test_pivot_around(self):
        pass

    def test_get_solution_primal(self):
        pass