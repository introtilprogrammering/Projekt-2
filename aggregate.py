## Data aggregation function

#slettes
import matplotlib.pyplot as plt
from dataload import load_measurements
import pandas as pd
import numpy as np

[tvec,data] = load_measurements("2008.csv", "drop")
periode = 'month'



tvec_a = []
data_a = []

if periode == 'month':
    tvec_a =[None]*12
    data_a = [None]*12
    for i in range (12):
        someData = data[tvec.month == i+1]
        someTvec = tvec[tvec.month == i+1]
        data_a[i] = someData.sum(axis = 0)
#        tvec_a = [x for x in tvec if tvec.month == i]

    data_a = pd.DataFrame(data = data_a)

while True