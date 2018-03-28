#!/usr/bin/ env python3.5
#Filename: utest_number_sequence.py

import unittest
import number_sequence as mod_test

class ValidatorTest(unittest.TestCase):
    def test_validator_positive_result(self):
        func_result = mod_test.validator('25')
        self.assertEqual(func_result, 25)
        
    def test_validator_negative_value(self):
        func_result = mod_test.validator('-25')
        self.assertEqual(func_result, None)
        
    def test_validator_zero_value(self):
        func_result = mod_test.validator('0')
        self.assertEqual(func_result, None)
        
    def test_validator_chars_but_int(self):
        func_result = mod_test.validator('s')
        self.assertEqual(func_result, None)
        
    def test_validator_float_but_int(self):
        func_result = mod_test.validator('100.125')
        self.assertEqual(func_result, None)
        
class SequenceGeneratorTest(unittest.TestCase):
    def test_obj_exists(self):
        func_result = mod_test.SequenceGenerator(25)
        self.assertEqual(isinstance(func_result, 
                                    mod_test.SequenceGenerator), True)
        
    def test_obj_value(self):
        func_result = mod_test.SequenceGenerator(25)
        self.assertEqual(func_result.n, 25)
        
    def test_sequence_func(self):
        func_result = mod_test.SequenceGenerator(25)
        self.assertEqual(func_result.sequence(), '0, 1, 2, 3, 4')
        


if __name__ == "__main__":
    unittest.main()
    
    