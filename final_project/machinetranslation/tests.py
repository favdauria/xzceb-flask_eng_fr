import unittest

from translator import english_to_french, french_to_english

class TestNull(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(english_to_french('None'), '   ')  
        self.assertNotEqual(french_to_english('None'), '   ')  

class TestHi(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french('Hello'),'Bonjour') 
        self.assertEqual(french_to_english('Bonjour'),'Hello') 

unittest.main()