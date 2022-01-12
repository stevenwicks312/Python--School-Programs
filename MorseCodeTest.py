import unittest
from WicksProjectPart1 import MorseToEnglish
from WicksProjectPart1 import EnglishToMorse

class Test(unittest.TestCase):

    def testOne(self):
        self.assertEqual(EnglishToMorse('TEST'), '- . ... - ')
        self.assertEqual(EnglishToMorse('test attempt two'),
                        "- . ... -  .- - - . -- .--. -  - .-- --- ")

    def testTwo(self):
        self.assertEqual(MorseToEnglish('--- -. .  - .-- ---  - .... .-. . . '),
                         'ONE TWO THREE ',)
        self.assertEqual(MorseToEnglish("..-. --- ..- .-.  ..-. .. ...- .  ... .. -..-"),
                         "FOUR FIVE SIX")
    def testNull(self):
        self.assertEqual(EnglishToMorse('1 2 3 4 5'), None)
        self.assertEqual(EnglishToMorse('. - . - .'), None)
        self.assertEqual(MorseToEnglish('A B C D E'), None)


if __name__ == '__main__':
    unittest.main()