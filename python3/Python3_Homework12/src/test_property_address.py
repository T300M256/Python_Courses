import unittest
from property_address import *
 
class TestAddresses(unittest.TestCase): 
   
    def setUp(self): 
        #self.home = Address( name='Steve Holden', street_address='1972 Flying Circus', city='Arlington', state='VA', zip_code='12345' )
        self.home = Address( name='Steve Holden', street_address='1972 Flying Circus', city='Arlington', state='VIR', zip_code='12345-1234' )
        #property_address.__main__('property_address.py -l WARNING -n Tom -a "my street" -c "San Diego" -s "CA" -z "EZ 123"')
        #OptionParser()
       
    def test_name(self): 
        self.assertEqual(self.home.name, 'Steve Holden') 
        self.assertRaises(AttributeError, setattr, self.home, 'name', 'Daniel Greenfeld')  
           
    def test_state(self): 
        self.assertEqual(self.home.state, 'VIR') 
        self.assertRaises(StateError, setattr, self.home, 'state', 'PA')  
        self.home.state = 'COL' 
        self.assertEqual(self.home.state, 'COL')  
        
    def test_zip_code(self): 
        self.assertEqual(self.home.zip_code, '12345-1234') 
        self.assertRaises(ZipCodeError, setattr, self.home, 'zip_code', '12345')   
        self.home.zip_code = '54321-1234' 
        self.assertEqual(self.home.zip_code, '54321-1234')
 
    def test_cli(self):
        parser = create_parser()
        (options, args) = parser.parse_args(['-l','WARNING', '-n', 'Tom', '-a', 'my street','-c', 'San Diego', '-s', 'CA', '-z', 'EZ 123'])
        result = valid_args(name=options.name, address=options.address, city=options.city, state=options.state, zip_code=options.zip_code)
        self.assertTrue(result, "Expected valid_args to return True")
        (options, args) = parser.parse_args(['-l','WARNING', '-n', 'Tom', '-a', 'my street','-c', 'San Diego', '-s', 'CA']) # missing zip
        result = valid_args(name=options.name, address=options.address, city=options.city, state=options.state, zip_code=options.zip_code)
        self.assertFalse(result, "Expected valid_args to return False")

if __name__ == "__main__": 
    start_logging(level="info")
    unittest.main()