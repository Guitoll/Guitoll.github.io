#!/bin/bash

conda activate bokeh2
path=/Users/fcuevas/Documents/Trabajo/thenergy/sun4heat/oemof/Coya_Sur/Escenario_1

cd $path
echo $PWD
bokeh serve plots_Esc1_CS.py --port 5002 & #--allow-websocket-origin=18.216.78.202:5510 &