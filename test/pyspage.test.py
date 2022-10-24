import sys
sys.path.append('..')


import pyspage
with open('pyspage.test.out.html', 'w') as f:
    html = pyspage.main('mock.py')
    f.write(html)
