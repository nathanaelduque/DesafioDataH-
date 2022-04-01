from script.check_PokerHand import PokerHand
from script.DefResult import Result
import unittest


class test(unittest.TestCase):
                    
   
    def test_first(self):
                
        # two pair x two pair
        self.assertTrue(PokerHand("TC TH 5C 5H KH").compare_with(PokerHand("9C 9H 5D 5S AC")) == Result.WIN)
        # one pair x one pair
        self.assertTrue(PokerHand("TS TD KC JC 7C").compare_with(PokerHand("JS JD AS KC TH")) == Result.LOSS)
        # one pair x one pair
        self.assertTrue(PokerHand("7H 7C QC JS TS").compare_with(PokerHand("7D 7S JH TH 6D")) == Result.WIN)
        # one pair x two pair
        self.assertTrue(PokerHand("5S 5D 8C 7S 6H").compare_with(PokerHand("7D 7H 5H 5C JS")) == Result.LOSS)
        # one pair x one pair
        self.assertTrue(PokerHand("AS AC KH 7D 3D").compare_with(PokerHand("AD AH KD 7C 4S")) == Result.LOSS)
        # royal straight flush x four of a kind
        self.assertTrue(PokerHand("TS JS QS KS AS").compare_with(PokerHand("9C 9H 9S 9D KH")) == Result.WIN)
        # royal straight flush x straight
        self.assertTrue(PokerHand("TS JS QS KS AS").compare_with(PokerHand("TC JD QC KC AC")) == Result.WIN)
        # royal straight flush x three of a kind
        self.assertTrue(PokerHand("TS JS QS KS AS").compare_with(PokerHand("QH QC QD AD 8H")) == Result.WIN)
        # four of a kind x straight
        self.assertTrue(PokerHand("AC AH AS AD KS").compare_with(PokerHand("9C TC JS QC KS")) == Result.WIN)
        # four of a kind x three of a kind
        self.assertTrue(PokerHand("AC AH AS AD KS").compare_with(PokerHand("QH QS QC KD 8H")) == Result.WIN)
        # straight x three of a kind
        self.assertTrue(PokerHand("TC JS QC KS AC").compare_with(PokerHand("QH QS QD AS 8H")) == Result.WIN)
        # straight flush x four of a kind
        self.assertTrue(PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("KH KC KS KD TD")) == Result.WIN)
        # straight flush x flush
        self.assertTrue(PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("4C 5C 9C TC JC")) == Result.WIN)
        # straight flush x straight
        self.assertTrue(PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("7C 8S 9S TC JC")) == Result.WIN) 
        # straight flush x
        self.assertTrue(PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("TS TH TD JH JD")) == Result.WIN)
        # straight flush x two pair
        self.assertTrue(PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("JC JD TD TC 4C")) == Result.WIN)
        # four of a kind x flush
        self.assertTrue(PokerHand("JH JC JS JD TH").compare_with(PokerHand("4H 5H 9H QH KH")) == Result.WIN)
        # four of a kind x straight
        self.assertTrue(PokerHand("JH JC JS JD TH").compare_with(PokerHand("5C 6S 7H 8H 9H")) == Result.WIN)
        # four of a kind x full house
        self.assertTrue(PokerHand("JH JC JS JD TH").compare_with(PokerHand("TS TC TD KH KD")) == Result.WIN)
        # four of a kind x two pair
        self.assertTrue(PokerHand("JH JC JS JD TH").compare_with(PokerHand("QH QD TD TC 4C")) == Result.WIN)
        # flush x straight
        self.assertTrue(PokerHand("4H 5H 9H TH JH").compare_with(PokerHand("7C 8S 9D TD JC")) == Result.WIN)
        # flush x full house
        self.assertTrue(PokerHand("4H 5H 9H TH JH").compare_with(PokerHand("TS TC TD JC JD")) == Result.LOSS)
        # flush x two pair
        self.assertTrue(PokerHand("4H 5H 9H TH JH").compare_with(PokerHand("JH JD TS TC 4C")) == Result.WIN)
        # straight x full house
        self.assertTrue(PokerHand("7C 8S 9H TH JH").compare_with(PokerHand("TS TC TD JC JD")) == Result.LOSS)
        # straight x two pair
        self.assertTrue(PokerHand("7C 8S 9H TH JH").compare_with(PokerHand("JC JD TS TC 4C")) == Result.WIN)
        # three of a kind x two pair
        self.assertTrue(PokerHand("TS TH TD JH JD").compare_with(PokerHand("JS JC KC KC 4C")) == Result.WIN)

if __name__ == '__main__':
    unittest.main()    

        
