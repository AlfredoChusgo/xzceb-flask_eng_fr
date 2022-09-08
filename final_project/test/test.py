import unittest
from machinetranslation.translator import english_to_french,french_to_english

class TestLanguageTranslator(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')
        self.assertNotEqual(english_to_french('Hello'),None)

    def test2(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello')
        self.assertNotEqual(french_to_english('Bonjour'),None)


unittest.main()