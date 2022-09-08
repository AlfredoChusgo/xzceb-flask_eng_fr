import unittest
import machinetranslation

class TestLanguageTranslator(unittest.TestCase):
    def test1(self):
        self.assertEqual(machinetranslation.english_to_french('Hello'),'Bonjour')
        self.assertNotEqual(machinetranslation.english_to_french('Hello'),None)

    def test2(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello')
        self.assertNotEqual(french_to_english('Bonjour'),None)


unittest.main()