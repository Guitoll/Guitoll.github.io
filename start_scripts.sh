#!/bin/bash

LAUNCH_SCRIPTS_ROUTE=/Users/fcuevas/Documents/Trabajo/thenergy/sun4heat/oemof/Coya_Sur/Calculadora/scripts;
pm2 start --name plots_Esc1_CS $LAUNCH_SCRIPTS_ROUTE/run_esc1.sh
pm2 start --name plots_Esc2A_CS $LAUNCH_SCRIPTS_ROUTE/run_esc2A.sh
pm2 start --name plots_Esc2B_CS $LAUNCH_SCRIPTS_ROUTE/run_esc2B.sh
pm2 start --name plots_Esc3A_CS $LAUNCH_SCRIPTS_ROUTE/run_esc3A.sh
pm2 start --name plots_Esc3B_CS $LAUNCH_SCRIPTS_ROUTE/run_esc3B.sh
pm2 start --name plots_Esc4_CS $LAUNCH_SCRIPTS_ROUTE/run_esc4.sh