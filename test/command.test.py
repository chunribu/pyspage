import sys
sys.path.append('..')


from pyspage import command
class A:
    file = 'mock.py'
    outdir = None
    localize = False
    server = False
    browser = False
args = A()
command.main(args)