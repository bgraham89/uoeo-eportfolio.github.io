'''
Helper file for making imports convenient.

Provides correct context to main imports. 
main.py and tests/context.py imports through this 
module. No other files do, to prevent circular imports.
'''

from pathlib import Path
import sys

path = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(path))

import app.components as components
import app.datastructures as datastructures
import app.helperfunctions.guards as guards