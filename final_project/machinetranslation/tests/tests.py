import unittest
from translator import englishToFrench, frenchToEnglish
class TestenglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench('Hello'),'Bonjour')
        self.assertEqual(englishToFrench('World'), 'Monde')
        self.assertEqual(englishToFrench(' '), ' ')
        
class TestfrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello')
        self.assertEqual(frenchToEnglish('Monde'), 'World')
        self.assertEqual(frenchToEnglish(' '), ' ')
        
unittest.main()