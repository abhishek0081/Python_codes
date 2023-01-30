import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data =pd.read_csv(r"D:\OneDrive\Desktop\python\em-9EhjTEemU7w7-EFnPcg_7aa34fc018d311e980c2cb6467517117_happyscore_income.csv");
data.sort_values("avg_income",inplace =True);
# print(data.head());
income = data["avg_income"];
happy = data["happyScore"];
income_happy = np.column_stack((income,happy))
km_res = KMeans(n_clusters=4).fit(income_happy);
richest = data[data['avg_income']> 15000];
all_mean = np.mean(data["avg_income"]);
ineq = data["income_inequality"];
plt.scatter(data["avg_income"],data["happyScore"],s = ineq*10,alpha = 0.25,color = "crimson");
plt.xlabel("income");
clusters = km_res.cluster_centers_;
plt.scatter(clusters[:,0],clusters[:,1],s =1000,alpha =0.5);
plt.ylabel("Happy Score");
for k,row in richest.iterrows():
    plt.text(row["avg_income"],row["happyScore"],row["country"])
plt.show();
