from pyspage.elements import Row, Column, Button
import matplotlib.pyplot as plt

layout = '''
row_a
    box
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
box = Column(class_='col-6')
btn_a = Button('CLICK a')
btn_b = Button('CLICK b')

btn_a.onclick = lambda e: print('a is clicked!')

def click_b(e):
    fig, ax = plt.subplots()
    fruits = ['apple', 'blueberry', 'cherry', 'orange']
    counts = [40, 100, 30, 55]
    ax.bar(fruits, counts)
    box.write(fig)
btn_b.onclick = click_b

def create_box():
    row_a.classList.add('bg-warning')
    box.write('This is the content.')
box.oncreate = create_box
