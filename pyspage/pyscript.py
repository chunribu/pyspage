from .layout import load_layout_str, all_elements

def get_elements(fpath):
    layout_str = load_layout_str(fpath)
    elements = all_elements(layout_str)
    return elements

def ele_in_line(line, eles):
    line = [j for i in line.split('=') for j in i.split() if j]
    for e in eles:
        if e == line[0]:
            return e
    return False

def select_element(ele):
    return f'{ele} = document.querySelector("#{ele}")\n'

def py2pys(fpath):
    script = ''
    elements = get_elements(fpath)
    with open(fpath) as f:
        bypass = False
        for line in f:
            if bypass:
                if ('"' in line) or ("'" in line):
                    bypass = False
                else:
                    continue
            elif line.strip().startswith('#'):
                script += '\n'
            elif ('pyspage' in line) and ('import' in line):
                continue
            elif ('layout' in line) and ('=' in line):
                bypass = True
                continue
            elif line.strip() == '':
                script += line
            elif ele_in_line(line, elements):
                ele = ele_in_line(line, elements)
                new_line = select_element(ele)
                script += new_line
            else:
                script += line
    return script
    