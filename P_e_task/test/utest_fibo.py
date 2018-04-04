#!/usr/bin/env python3.5
# Filename: utest_fibo.py
# Usage from P_e_task: python3 -m P_e_task.test.utest_envelopes

import unittest
from ..task import fibo as mod_test


class FiboTest(unittest.TestCase):
    def test_obj_exists(self):
        func_result = mod_test.Fibo(4, 4)
        self.assertEqual(isinstance(func_result, 
                                    mod_test.Fibo), True)
        
    def test_obj_height(self):
        func_result = mod_test.Fibo(4, 5)
        self.assertEqual(func_result.low, 4)
        
    def test_obj_width(self):
        func_result = mod_test.Fibo(4, 5)
        self.assertEqual(func_result.high, 5)
        
    def test_fibo_shape_func(self):
        func_result = mod_test.Fibo(5, 10)
        expected_res = '3, 5, 8, 13, 21, 34'
        self.assertEqual(func_result.fibo_shape(), expected_res)
        

if __name__ == '__main__':
    unittest.main()
