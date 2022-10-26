import sys
sys.path.append('..')


from pyspage import *
layout = '''
row_
    col_a
        input_
        textarea_
        multi_
    col_b
        file_
        one_
        t_1
        btn_
'''
row_ = Row()
col_a = Column(4)
col_b = Column(8)
input_ = Input('input here')
file_ = File('select file')
textarea_ = Textarea()
one_ = SelectOne(['A','B','C'], default_index=1)
multi_ = SelectMulti(['A','B','C'], default_index=[0,1])
t_1 = Text('This is a test!')
btn_ = Button()
    
row_.oncreate = lambda e: row_.classList.add('bg-warning')

btn_.onclick = lambda e: print(one_.elements.index.value)