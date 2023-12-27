# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 10:48:27 2023

@author: Diego
"""

import os 
import sys
sys.path
path = os.getcwd()
sun4heat_path = os.path.dirname(os.path.dirname(os.path.dirname(path)))
script_path = os.path.join(sun4heat_path,'scripts')
sys.path.append(script_path)
path = os.path.join(path,'')
path=os.path.dirname(os.path.dirname(path))
path = os.path.join(path,'')

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#---------------------------------------- IMPORTAMOS LIBRERIAS RELEVANTES ---------------------------------------------
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#

import numpy_financial as npf
import numpy as np
import pandas as pd
from scipy.optimize import minimize, rosen, rosen_der, Bounds
from bokeh.plotting import figure
from bokeh.models.widgets import  Select, Button, CheckboxButtonGroup, TableColumn, NumberFormatter, DataTable, PreText
from bokeh.models import DatetimeTickFormatter, LinearColorMapper, ColorBar, BasicTicker, PrintfTickFormatter, TextInput, HoverTool, Spacer, RadioButtonGroup
from bokeh.layouts import column, gridplot, row
from bokeh.transform import factor_cmap
from bokeh.palettes import Category20
from bokeh.models import ColumnDataSource, TabPanel, Tabs
from bokeh.models import FactorRange
from bokeh.io import curdoc
from bokeh.models import LinearAxis, Range1d

df=pd.read_csv(os.getcwd()+"/Demo_Thenergy/static/resultados_oemof_Carozzi.csv")
df['fecha']=pd.to_datetime(df.iloc[:,0])
source = ColumnDataSource(df.iloc[:3,:])


alpha_line = 0.6
p1 = figure(width=1000, height=450, title="Stream Online Sensor",y_axis_label="Potencia proceso (MW)")
p1.title.text_font_size = "20px"

line1_p1 = p1.line(x='fecha',y='hw__el_wtB',source=source,color='green',legend_label='HW desde Caldera 1 (MW)', line_alpha=alpha_line)
line1_p1.visible = True
line1_p2 = p1.line(x='fecha',y='cm__rgas',source=source,color='orange',legend_label='Flujo combustible (MW)', line_alpha=alpha_line)
line1_p2.visible = True
p1.xaxis.formatter=DatetimeTickFormatter()


i=4
def update():
    global i
    line1_p1.data_source.data=df.iloc[:i,:]
    line1_p2.data_source.data=df.iloc[:i,:]
    i=i+1
    

layout=column(p1)
curdoc().add_root(layout)
curdoc().add_periodic_callback(update,1000)





    