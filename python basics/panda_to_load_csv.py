import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data =pd.read_csv("em-9EhjTEemU7w7-EFnPcg_7aa34fc018d311e980c2cb6467517117_happyscore_income.csv");
# print(data);
happy =  data['happyScore'];
income = data['avg_income'];
print(happy.max());
print(income.max());
plt.scatter(income,happy);
plt.xlabel("income");
plt.ylabel("Happiness");
plt.show();

