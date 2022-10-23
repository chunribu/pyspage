import sys
sys.path.append('..')


from pyspage.layout import parse_layout, gen_id_dict, id_dict_to_html

ind_and_id = parse_layout('mock.py')
root = gen_id_dict(ind_and_id)
html = id_dict_to_html('mock.py', root)
print(html)