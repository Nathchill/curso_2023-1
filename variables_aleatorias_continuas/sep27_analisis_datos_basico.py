# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 08:31:22 2022

@author: b12s301e19
"""

"""
Datos:
    
4.33  4.38  4.48  4.48  4.50  4.55  4.59  4.59  4.61  4.61
4.75  4.76  4.78  4.82  4.82  4.83  4.86  4.93  4.94  4.94
4.94  4.96  4.97  5.00  5.01  5.02  5.05  5.06  5.08  5.09
5.10  5.12  5.13  5.15  5.15  5.15  5.16  5.16  5.16  5.18
5.19  5.23  5.24  5.29  5.32  5.33  5.35  5.37  5.37  5.39
5.41  5.43  5.44  5.46  5.46  5.47  5.50  5.51  5.53  5.55
5.55  5.56  5.61  5.62  5.64  5.65  5.65  5.66  5.67  5.67
5.68  5.69  5.70  5.75  5.75  5.75  5.76  5.76  5.79  5.80
5.81  5.81  5.81  5.81  5.85  5.85  5.90  5.90  6.00  6.03
6.03  6.04  6.04  6.05  6.06  6.07  6.09  6.13  6.21  6.34
6.43  6.61  6.62  6.65  6.81

"""


import numpy as np
import pandas as pd
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt
d = [4.33,  4.38,  4.48,  4.48,  4.50,  4.55,  4.59,  4.59,  4.61,  4.61,
     4.75,  4.76,  4.78,  4.82,  4.82,  4.83,  4.86,  4.93,  4.94,  4.94,
     4.94,  4.96,  4.97,  5.00,  5.01,  5.02,  5.05,  5.06,  5.08,  5.09,
     5.10,  5.12,  5.13,  5.15,  5.15,  5.15,  5.16,  5.16,  5.16,  5.18,
     5.19,  5.23,  5.24,  5.29,  5.32,  5.33,  5.35,  5.37,  5.37,  5.39,
     5.41,  5.43,  5.44,  5.46,  5.46,  5.47,  5.50,  5.51,  5.53,  5.55,
     5.55,  5.56,  5.61,  5.62,  5.64,  5.65,  5.65,  5.66,  5.67,  5.67,
     5.68,  5.69,  5.70,  5.75,  5.75,  5.75,  5.76,  5.76,  5.79,  5.80,
     5.81,  5.81,  5.81,  5.81,  5.85,  5.85,  5.90,  5.90,  6.00,  6.03,
     6.03,  6.04,  6.04,  6.05,  6.06,  6.07,  6.09,  6.13,  6.21,  6.34,
     6.43,  6.61,  6.62,  6.65,  6.81]


df = pd.DataFrame(data=d,
                  columns=["datos"])


plt.figure()
ax = sns.histplot(data = df, 
             x="datos",
             bins = 8,
             kde=True)
ax.lines[0].set_color('crimson')



# Medias
media = df.mean()
varianza = df.var()
sd = df.std()

#  Metricas basicas
print("Media de los datos:", media[0])
print("Varianza de los datos:", varianza[0])
print("Desviacion estandar de los datos:", sd[0])
print()
# Informacion
print(df.describe())
