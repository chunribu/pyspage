from pyspage.elements import Row, Column, Button
import time

layout = '''
row_a
row_b
    col_a
        btn_a
    col_b
        btn_b
'''

row_a = Row()
row_b = Row()
col_a = Column()
col_b = Column()
btn_a = Button('CLICK a')
btn_b = Button('CLICK b')

btn_a.onclick = lambda e: print('a is clicked!')
def click_b(e):
    print('b is clicked!')
btn_b.onclick = click_b
row_a.oncreate = lambda e: row_a.classList.add('bg-warning')
row_a.write('This is the content.')
