"""
property address homework
"""
import re, logging, configparser
from optparse import OptionParser

config = configparser.RawConfigParser()
config.read('V:/workspace/Python3_Homework12/src/property_address.cfg')

LOG_FILENAME = config.get('log', 'output')
LOG_FORMAT = config.get('log', 'format')
zip_valid_pattern = config.get('validators', 'zip_code')
state_valid_pattern = config.get('validators', 'state')

DEFAULT_LOG_LEVEL = "error" # Default log level
LEVELS = {'debug': logging.DEBUG,
          'info': logging.INFO,
          'warning': logging.WARNING,
          'error': logging.ERROR,
          'critical': logging.CRITICAL,
          'DEBUG': logging.DEBUG,
          'INFO': logging.INFO,
          'WARNING': logging.WARNING,
          'ERROR': logging.ERROR,
          'CRITICAL': logging.CRITICAL
          }

def start_logging(filename=LOG_FILENAME, level=DEFAULT_LOG_LEVEL):
    "Start logging with given filename and level."
    logging.basicConfig(filename=filename, level=LEVELS[level], format=LOG_FORMAT)
    # log a message
    #logging.info('Starting up the property_address module')

class ZipCodeError(Exception):
    pass

class StateError(Exception):
    pass

class Address(object):
    def __init__(self, name='', street_address='', city='', state='', zip_code=''):
        logging.info("Creating a new address")
        self._name = name
        self._street_address = street_address
        self._city = city
        self._state = state
        self._zip_code = zip_code
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if self._name == '':
            self._name = value
        else:
            raise AttributeError
    
    @property
    def street_address(self):
        return self.street_address
    
    @street_address.setter
    def street_address(self, value):
        self._street_address = value
    
    @property
    def city(self):
        return self.city
    
    @city.setter
    def city(self, value):
        self._city = value
    
    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self, value):
        #if re.match("^[A-Z][A-Z]$", value):
        if re.match(state_valid_pattern, value):
            self._state = value
        else:
            logging.error("STATE exception")
            raise StateError
        
    
    @property
    def zip_code(self):
        return self._zip_code
    
    @zip_code.setter
    def zip_code(self, value):
        logging.info("validating zip code: "+value)
        if re.match(zip_valid_pattern, value):
            self._zip_code = value
        else:
            logging.error("ZIPCODE exception")
            raise ZipCodeError
    
def create_parser():
    
    parser = OptionParser()
    parser.add_option('-l', '--level', dest="level", action="store", default="info", help="Levels: DEBUG, INFO, WARNING, ERROR, and CRITICAL")
    parser.add_option('-n', '--name', dest="name", action="store", help="Name of addressee")
    parser.add_option('-a', '--address', dest="address", action="store", help="Address")
    parser.add_option('-c', '--city', dest="city", action="store", help="City")
    parser.add_option('-s', '--state', dest="state", action="store", help="State must be valid")
    parser.add_option('-z', '--zip_code', dest="zip_code", action="store", help="Must be valid US zip code")
    return parser 

def valid_args(**kwargs):
    if None in (kwargs['name'], kwargs['address'], kwargs['city'], kwargs['state'], kwargs['zip_code']):
        return(False)
    else:
        return(True)

if __name__ == "__main__":
    parser = create_parser()
    (options, args) = parser.parse_args()
    # validation        
    if not valid_args(name=options.name, address=options.address, city=options.city, state=options.state, zip_code=options.zip_code):
        parser.error("options -n, -a, -c, -s, -z are required")
    # run the program
    start_logging(level=options.level)

    try:
        ad = Address(name=options.name, street_address=options.address, city=options.city, state=options.state, zip_code=options.zip_code )
    except ZipCodeError:
        parser.error("option -z requires a valid US zip code")

    print("Created address for",ad.name, "at zip code", ad.zip_code)