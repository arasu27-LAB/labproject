# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 12:58:00 2025

@author: PSVCS01
"""
import pandas as pd
data = {
 "calories": [420, 380, 390],
 "duration": [50, 40, 45]
}
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df.loc["day2"])