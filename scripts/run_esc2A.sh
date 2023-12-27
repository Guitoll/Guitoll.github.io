#!/bin/bash

conda activate bokeh2
path=/Users/fcuevas/Documents/Trabajo/thenergy/sun4heat/oemof/Coya_Sur/Escenario_2A

cd $path
echo $PWD
bokeh serve plots_Esc2A_CS.py --port 5003 & #--allow-websocket-origin=18.216.78.202:5510 &