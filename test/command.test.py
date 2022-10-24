import sys
sys.path.append('..')


from pyspage import command
class A:
    file = 'mock.py'
    output = None
    localize = False
    server = True
    browser = True
args = A()
command.main(args)