import sys
import time
from django.test import TestCase


def animated_loading():
    
    chars = "/—\|" 
    for char in chars:
        sys.stdout.write('\r'+'loading...'+char)
        time.sleep(.1)
        sys.stdout.flush() 
animated_loading()


