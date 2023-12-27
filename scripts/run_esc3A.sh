#!/bin/bash

conda activate bokeh2
path=/Users/fcuevas/Documents/Trabajo/thenergy/sun4heat/oemof/Coya_Sur/Escenario_3A

cd $path
echo $PWD
bokeh serve plots__Esc3A_CS.py --port 5005 & #--allow-websocket-origin=18.216.78.202:5510 &