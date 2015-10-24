import unittest

import logging
from ivy.ivy import ivylogger

"""
This is the main test script. It discovers and runs all of the unit
tests. New tests can be put in the tests folder: just make sure the 
filename starts with "test".
"""

def main():
    ivylogger.setLevel(logging.CRITICAL) # Disable logging

    loader = unittest.TestLoader()
    tests = loader.discover('tests/')
    testRunner = unittest.runner.TextTestRunner()
    testRunner.run(tests)

if __name__ == '__main__':
    main()