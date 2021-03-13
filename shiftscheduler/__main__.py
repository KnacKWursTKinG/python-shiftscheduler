
import sys
import os

sys.path.insert(0, os.path.abspath(__file__).rsplit('/', 2)[0])
from shiftscheduler import entry_point
sys.path.pop(0)

entry_point()
