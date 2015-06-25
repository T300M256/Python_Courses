"""
Simple bunch class with a pretty print method that protects its API
"""
import unittest

class Bunch(object):
    def __init__(self, *args,**kwargs):
        #self.__dict__.update(kwargs)
        for key, value in kwargs.items():
            if hasattr(self, key):
                raise AttributeError("API conflict: '%s' is part of the '%s' API" % (key, self.__class__.__name__))
            else:
                setattr(self, key, value)

    def pretty(self):            
        text = ""
        for key, value in self.__dict__.items():
            text += "%s: %s\n" % (key, value)
        return text

class TestBunch(unittest.TestCase):
    def test_attributes(self):
        b = Bunch(name="Python 3", language="Python 3.0.1")
        self.assertEqual("Python 3", b.name)
        self.assertEqual("Python 3.0.1", b.language)
    def test_pretty(self):
        self.assertRaises(AttributeError, Bunch, name="Audrey", job="Software Developer", pretty=True)
        b = Bunch(name="Steve Holden", profession="Pythonista")
        p = b.pretty()
        self.assertTrue("name: Steve Holden" in p)
        self.assertTrue("profession: Pythonista" in p)
        self.assertEqual(len(p.splitlines()), 2, "Too many lines in output")


if __name__ == "__main__":
    unittest.main()