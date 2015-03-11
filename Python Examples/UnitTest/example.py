__author__ = 'jim'

import unittest

class FooTest(unittest.TestCase):
    """Sample test case"""

    # preparing to test
    def setUp(self):
        """ Setting up for the test """
        print "FooTest:setUp_:begin"
        ## do something...
        print "FooTest:setUp_:end"

    # ending the test
    def tearDown(self):
        """Cleaning up after the test"""
        print "FooTest:tearDown_:begin"
        ## do something...
        print "FooTest:tearDown_:end"

    # test routine A
    def testA(self):
        """Test routine A"""
        print "FooTest:testA"
        self.assertNotEqual(10,10,"These are equal")

    # test routine B
    def testB(self):
        """Test routine B"""
        print "FooTest:testB"

    def testtest(self):
        """Test routine test"""
        print "FooTest:testest"




if __name__ == "__main__":
    unittest.main()