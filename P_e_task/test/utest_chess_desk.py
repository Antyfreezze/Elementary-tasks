#!/usr/bin/env python3.5
# Filename: utest_chess_desk.py
# Usage from P_e_task: python3 -m P_e_task.test.utest_chess_desk

import unittest
from ..task import chess_desk as mod_test


class FieldGeneratorTest(unittest.TestCase):
    def test_obj_exists(self):
        func_result = mod_test.FieldGenerator(4, 4)
        self.assertEqual(isinstance(func_result, 
                                    mod_test.FieldGenerator), True)
        
    def test_obj_height(self):
        func_result = mod_test.FieldGenerator(4, 5)
        self.assertEqual(func_result.height, 4)
        
    def test_obj_width(self):
        func_result = mod_test.FieldGenerator(4, 5)
        self.assertEqual(func_result.width, 5)
        
    def test_string_concat_func(self):
        func_result = mod_test.FieldGenerator(2, 5)
        expected_res = '* * * * * \n * * * * *\n'
        self.assertEqual(func_result.string_concat(), expected_res)
        

if __name__ == '__main__':
    unittest.main()
