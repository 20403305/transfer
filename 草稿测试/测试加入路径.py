import os
import sys

#1
sys.path.extend([os.path.join(root, name) for root, dirs, _ in os.walk("..") for name in dirs]) 

[print(path) for path in sys.path]

#2
sys.path.insert(0, os.path.realpath('.'))#有的IDE很乱，这个加上去保险！！
sys.path.insert(0, os.path.realpath('..'))

[print(path) for path in sys.path]

#3
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
[print(path) for path in sys.path]