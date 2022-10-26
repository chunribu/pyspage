import sys
sys.path.append('..')


f = 'element_test.py'

from pyspage import command
class A:
    file = f
    output = None
    localize = False
    server = True
    browser = True
args = A()
command.main(args)