# -*- coding: utf-8 -*-
"""
Created on June 04 2021
Flow Duration Multiplot  (v1)
@author: tclarkin (USBR 2021)

This script allows the user to plot multiple annual duration curves
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
from functions import plot_dur_ep,get_varlabel

### Begin User Input ###
#os.chdir("C://Users//tclarkin//Documents//Projects//Anderson_Ranch_Dam//duration_analyses//")

# Site information and user selections
sites = ["ARD","ARD_USGS","NRNI"] # list, site or dam names
labels = ["Flow","Flow (USGS)","Flow (BPA)"] # labels for sites

### Begin Script ###
# Check for output directory
if not os.path.isdir("flow"):
    print("duration directory does not exist. Please run 2a_flow_duration_analysis.py before using this script.")

# Initiate plot
plot_dur_ep()

# Loop through sites
var = None
for site,label in zip(sites,labels):
    data = pd.read_csv(f"flow/{site}_annual_raw.csv",parse_dates=True,index_col=0)
    if var is None:
        var = data.columns[1]
        var_label = get_varlabel(var)
    else:
        if data.columns[1]!=var:
            var = data.columns[1]
            var_label = f"{var_label} | {get_varlabel(var)}"
    plt.plot(data.exceeded*100,data[var],label=label)
plt.ylabel(var_label)
plt.legend()
plt.savefig(f"flow/all_annual_multiplot.jpg",bbox_inches='tight',dpi=600)
