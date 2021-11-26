import unittest
from translator import englist_to_french as englistToFrench, french_to_english as FrenchToEnglish
class TestenglistToFrench(unittest.TestCase):
    def Test1(self):
        self.assertEqual('','')
        self.assertEqual('Hello','Bonjour')
class TestFrenchToEnglish(unittest.TestCase):
    def Test1(self):
        self.assertEqual('','')
        self.assertEqual('Bonjour','Hello')

unittest.main()