# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 17:42:43 2021

@author: Gourav
"""

#FindRelationBetweenAnyTwoNumericalColumnsWRTToOtherColumns

import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
sns.set(style="darkgrid")
fmri=sns.load_dataset("fmri")
print(fmri.head())
sns.relplot(x="timepoint",y="signal",data=fmri,hue="subject")
sns.relplot(x="timepoint",y="signal",kind="line",data=fmri)
sns.scatterplot(x="timepoint",y="signal",data=fmri)
sns.catplot(x="timepoint",y="signal",data=fmri)