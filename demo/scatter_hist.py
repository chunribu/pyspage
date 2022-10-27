from pyspage import *
import pandas as pd
import altair as alt
from vega_datasets import data

layout = '''
row_main
    title_
    col_left
        t_intro
        btn_ok
        btn_demo
    col_right
'''

row_main = Row()
title_ = Text('Facetted Scatterplot with marginal histograms', 5, class_='text-danger')
t_intro = Text('Figure is drawn from the iris dataset, you can click the buttons below to see the figure and the data.')
col_left = Column(class_ = 'col-md-4')
col_right = Column(class_ = 'col-md-8')
btn_ok = Button('Draw Fig')
btn_demo = Button('Show Data')

def draw_fig(e):
    source = data.iris()
    
    x_col = source.columns[0]
    y_col = source.columns[1]
    c_col = source.columns[-1]
    base = alt.Chart(source)
    xscale = alt.Scale(domain=(source.iloc[:,0].min(), source.iloc[:,0].max()))
    yscale = alt.Scale(domain=(source.iloc[:,1].min(), source.iloc[:,1].max()))

    points = base.mark_circle().encode(
        alt.X(x_col, scale=xscale),
        alt.Y(y_col, scale=yscale),
        color=c_col
    )

    bar_args = {'opacity': .3, 'binSpacing': 0}
    top_hist = base.mark_bar(**bar_args).encode(
        alt.X(x_col+':Q',
            bin=alt.Bin(maxbins=20, extent=xscale.domain),
            stack=None,
            title=''
            ),
        alt.Y('count()', stack=None, title=''),
        alt.Color(c_col+':N'),
    ).properties(height=60)

    right_hist = base.mark_bar(**bar_args).encode(
        alt.Y(y_col+':Q',
            bin=alt.Bin(maxbins=20, extent=yscale.domain),
            stack=None,
            title='',
            ),
        alt.X('count()', stack=None, title=''),
        alt.Color(c_col+':N'),
    ).properties(width=60)

    fig = top_hist & (points | right_hist)
    col_right.innerHTML = ''
    col_right.write(fig)

def show_demo_data(e):
    source = data.iris()
    col_right.innerHTML = ''
    col_right.write(source)

btn_ok.onclick = draw_fig
btn_demo.onclick = show_demo_data
row_main.oncreate = draw_fig