from pyspage.elements import Box, Button
import time

layout = '''
box_a
    btn_b
    btn_c
'''

box_a = Box()
btn_b = Button('CLICK B')
btn_c = Button('CLICK C')

btn_b.onclick = lambda e: print('B is clicked!')
def click_c(e):
    print('C is clicked!')
btn_c.onclick = click_c
