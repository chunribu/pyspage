import sys
sys.path.append('..')


from pyspage.pyscript import py2pys
with open('test_pyscript.out.py', 'w') as f:
    f.write(py2pys('./mock.py'))