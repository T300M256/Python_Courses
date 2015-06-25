"""
property address homework
"""
import re, logging

LOG_FILENAME = "property_address.log"
LOG_FORMAT = "%(asctime)s - %(levelname)s -  %(funcName)s - %(message)s"
DEFAULT_LOG_LEVEL = "error" # Default log level
LEVELS = {'debug': logging.DEBUG,
          'info': logging.INFO,
          'warning': logging.WARNING,
          'error': logging.ERROR,
          'critical': logging.CRITICAL
          }

def start_logging(filename=LOG_FILENAME, level=DEFAULT_LOG_LEVEL):
    "Start logging with given filename and level."
    logging.basicConfig(filename=filename, level=LEVELS[level], format=LOG_FORMAT)
    # log a message
    #logging.info('Starting up the property_address program')

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
        if re.match("^[A-Z][A-Z]$", value):
            self._state = value
        else:
            logging.error("STATE exception")
            raise StateError
        
    
    @property
    def zip_code(self):
        return self._zip_code
    
    @zip_code.setter
    def zip_code(self, value):
        if re.match("^\d\d\d\d\d$", value):
            self._zip_code = value
        else:
            logging.error("ZIPCODE exception")
            raise ZipCodeError
    

        