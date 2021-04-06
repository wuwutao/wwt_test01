import unittest
from unit_leap_year import Is_leap


class Test_leap(unittest.TestCase):

    def test_2000(self):
        ly=Is_leap(2000)
        result=ly.pandan()
        self.assertEqual(result,"2000是闰年")

    def test_2013(self):
        ly=Is_leap(2013)
        result=ly.pandan()
        self.assertEqual(result,"2013不是闰年")
    
    def test_2400(self):
        ly=Is_leap(2400)
        result =ly.pandan()
        self.assertEqual(result,"2400不是闰年")

#封装
if __name__=='__main__':
    #调用suit 封装
    suit = unittest.TestSuite()
    suit.addTest(Test_leap("test_2000"))
    suit.addTest(Test_leap("test_2013"))
    suit.addTest(Test_leap("test_2400"))
    
    runner=unittest.TextTestRunner()
    runner.run(suit)