#!/bin/bash

conda activate bokeh2
path=/Users/fcuevas/Documents/Trabajo/thenergy/sun4heat/oemof/Coya_Sur/Escenario_3B

cd $path
echo $PWD
bokeh serve plots__Esc3B.py --port 5006 & #--allow-websocket-origin=18.216.78.202:5510 &