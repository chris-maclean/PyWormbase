import unittest
import os

os.chdir(os.path.dirname(__file__))

loader = unittest.TestLoader()
start_dir = '.'
suite = loader.discover(start_dir, pattern='*_tests.py')

runner = unittest.TextTestRunner()
runner.run(suite)
