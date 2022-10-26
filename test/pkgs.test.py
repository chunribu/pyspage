import sys
sys.path.append('..')


import pyspage
pkgs = pyspage.get_pkgs('mock.py')
print(pkgs)