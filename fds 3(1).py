# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 12:30:42 2025

@author: PSVCS01
"""

import pandas as pd
data = {
 "calories": [420, 380, 390],
 "duration": [50, 40, 45]
}
#load data into a DataFrame object:
df = pd.DataFrame(data)
print(df)
