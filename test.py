import unittest
import countNumOfVowls
import countStrOf_iti
import locationsOf_i
import removeVowls

class testCalc(unittest.TestCase):
    def test_count(self):
        self.assertEqual(countNumOfVowls.countV("ahmed Hegab"), 4, "should be 4")
        self.assertEqual(countStrOf_iti.countITI("itiititi"), 3, "should be 3")
    def test_removeV(self):
        self.assertEqual(removeVowls.removeV("ahmed mohammed"), "hmd mhmmd", "should be: hmd mhmmd")
    def test_locateI(self):
        self.assertEqual(locationsOf_i.locateI("heillo woirld"), [2, 9], "should be: [2, 9]")
        
    

if __name__ == "__main__":
    unittest.main()