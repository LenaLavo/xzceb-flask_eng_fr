import unittest

from translator import englishToFrench
class test_englishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        self.assertEqual(englishToFrench('0'), '0')

from translator import frenchToEnglish
class test_frenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        self.assertEqual(frenchToEnglish('0'), '0')

class test2_frenchToEnglish(unittest.TestCase):
    def test2(self):
        self.assertNotEqual(frenchToEnglish('Bonjour'), 'Bye')

class test2_englishToFrench(unittest.TestCase):
    def test2(self):
        self.assertNotEqual(englishToFrench('Hello'), 'Au revoir')

unittest.main()

