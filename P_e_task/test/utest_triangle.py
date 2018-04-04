#!/usr/bin/env python3.5
# Filename: utest_triangle.py
# usage from P_e_task: $ python3 -m P_e_task.test.utest_triangle

import unittest
from ..task import triangle as mod_test


class ValidatorTest(unittest.TestCase):
    def test_validator_positive_result(self):
        chk_lst = ['first', '2', '2', '2']
        expected_res = ['first', 2, 2, 2]
        func_result = mod_test.validator(chk_lst)
        self.assertEqual(func_result, expected_res)

    def test_validator_float_value(self):
        chk_lst = ['first', '1.5', '1.5', '1.5']
        expected_res = ['first', 1.5, 1.5, 1.5]
        func_result = mod_test.validator(chk_lst)
        self.assertEqual(func_result, expected_res)
        
    def test_validator_blank_item(self):
        chk_lst = ['first', '2', '2', '']
        message = "Too few parameters"
        with self.assertRaises(ValueError, msg=message):
            mod_test.validator(chk_lst)

    def test_validator_negative_value(self):
        chk_lst = ['first', '-1', '2', '2']
        message = "Use positive integers or floating point numbers"
        with self.assertRaises(ValueError, msg=message):
            mod_test.validator(chk_lst)

    def test_validator_zero_value(self):
        chk_lst = ['first', '2', '0', '2']
        message = "Use positive integers or floating point numbers"
        with self.assertRaises(ValueError, msg=message):
            mod_test.validator(chk_lst)

    def test_validator_chars_but_int(self):
        chk_lst = ['first', 's', '2', '2']
        message = "Use positive integers or floating point numbers"
        with self.assertRaises(ValueError, msg=message):
            mod_test.validator(chk_lst)
            
        
class CheckTrianglePossibleTest(unittest.TestCase):
    def test_triangle_cannot_exist(self):
        chk_lst = [5, 2, 2]
        message = "Triangle cannot exist"
        with self.assertRaises(ValueError, msg=message):
            mod_test.check_triangle_possible(*chk_lst)


if __name__ == '__main__':
    unittest.main()
