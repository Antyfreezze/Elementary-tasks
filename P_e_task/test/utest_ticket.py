#!/usr/bin/ env python3.5
# Filename: utest_ticket.py
# Usage from P_e_task: python3 -m P_e_task.test.utest_ticket

import os
import unittest
from ..task import ticket as mod_test

path = os.path.dirname(__file__) + '/Resources/About'


class ValidatorTest(unittest.TestCase):
    def test_validator_positive_result(self):
        func_result = mod_test.validator(path, '0', '202202')
        expected_res = [path, 0, 202202]
        self.assertEqual(func_result, expected_res)
        
    def test_validator_path_none(self):
        func_result = mod_test.validator('0', '0', '202202')
        self.assertEqual(func_result, None)
        
    def test_validator_path_not_exists(self):
        func_result = mod_test.validator('ssss', '0', '202202')
        self.assertEqual(func_result, None)
        
    def test_validator_zero_value(self):
        func_result = mod_test.validator(path, '0', '0')
        expected_res = [path, 0, 0]
        self.assertEqual(func_result, expected_res)
        
    def test_validator_chars_but_int(self):
        func_result = mod_test.validator(path, 's', '1')
        self.assertEqual(func_result, None)
        
    def test_validator_float_but_int(self):
        func_result = mod_test.validator(path, '0', '100.125')
        self.assertEqual(func_result, None)


class LuckyTicketListTest(unittest.TestCase):
    def test_lucky_ticket_list(self):
        func_result = mod_test.lucky_ticket_list('p', 0, 0)
        self.assertEqual(func_result, 1)
        

if __name__ == "__main__":
    unittest.main()
