import pandas as pd
from matplotlib import colors
import numpy as np
import matplotlib.pyplot as plt
fb = pd.read_csv('D:\\OneDrive\\Desktop\\financial_statistics_using_python\\facebook.csv',index_col=0);
ms = pd.read_csv('D:\\OneDrive\\Desktop\\financial_statistics_using_python\\microsoft.csv',index_col=0);
# print(ms)
# print(fb.head())
# print(fb.index[779])
# print(fb.columns)
# print(fb.shape)  #numbers of rows and numbers of columns
fb.tail();
#describe method

print(fb.describe());

#slicing data
# selection by label      .loc    
#  selection by position   .iloc
#slicing data frames


