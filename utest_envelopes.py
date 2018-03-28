#!/usr/bin/env python3.5
#Filename: utest_envelopes.py

import envelopes
import unittest


class EnvelopeTest(unittest.TestCase):
    
    def test_validator_positive_result(self):
        chk_lst = ['1', '2', '3', '4']
        func_result = envelopes.validator(chk_lst)
        self.assertEqual(func_result, chk_lst)
    
    def test_validator_blank_item(self):
        chk_lst = ['1', '2', '3', '']
        func_result = envelopes.validator(chk_lst)
        self.assertEqual(func_result, None)
        
    def test_validator_negative_value(self):
        chk_lst = ['-1', '2', '3', '4']
        func_result = envelopes.validator(chk_lst)
        self.assertEqual(func_result, None)
        
    def test_validator_zero_value(self):
        chk_lst = ['1', '0', '3', '4']
        func_result = envelopes.validator(chk_lst)
        self.assertEqual(func_result, None)
        
    def test_validator_chars_but_int(self):
        chk_lst = ['1', '2', 's', '4']
        func_result = envelopes.validator(chk_lst)
        self.assertEqual(func_result, None)
    
    def test_compare_first_in_second(self):
        chk_lst = [3, 4, 1, 2]
        func_result = envelopes.compare(*chk_lst)
        self.assertEqual(func_result, 'Second can be placed in first')
        
    def test_compare_second_in_first(self):
        chk_lst = [1, 2, 3, 4]
        func_result = envelopes.compare(*chk_lst)
        self.assertEqual(func_result, 'First can be placed in second')
        
    def test_compare_placed_diagonal(self):
        chk_lst = [1, 5, 4, 4]
        func_result = envelopes.compare(*chk_lst)
        self.assertEqual(func_result, 'First can be placed in second')
        
    def test_compare_cannot_placed(self):
        chk_lst = [11, 2, 3, 4]
        func_result = envelopes.compare(*chk_lst)
        self.assertEqual(func_result, 'Cannot be placed')
    
if __name__ == '__main__':
    unittest.main()
    
    