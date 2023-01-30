import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data =pd.read_csv(r"D:\OneDrive\Desktop\python\em-9EhjTEemU7w7-EFnPcg_7aa34fc018d311e980c2cb6467517117_happyscore_income.csv");
data.sort_values("avg_income",inplace =True);
print(data.head());

richest = data[data['avg_income']> 15000];
print(richest);

richest.iloc[0]; ## first country with the lowest income

richest.iloc[-1];  ## Last countryb with the Highest income

print(np.mean(richest["avg_income"]));
all_mean = np.mean(data["avg_income"]);
print(all_mean);
plt.scatter(richest["avg_income"],richest["happyScore"]);
plt.text(richest.iloc[0]["avg_income"],richest.iloc[0]["happyScore"],richest.iloc[0]["country"]);

plt.show();
plt.scatter(richest["avg_income"],richest["happyScore"]);
plt.text(richest.iloc[-1]["avg_income"],richest.iloc[-1]["happyScore"],richest.iloc[-1]["country"]);

plt.show();

plt.scatter(richest["avg_income"],richest["happyScore"]);
for k,row in richest.iterrows():
    plt.text(row["avg_income"],row["happyScore"],row["country"])
    print(row["country"])
plt.show();
ineq = data["income_inequality"];
### Eyeballing data
plt.xlabel("income");
plt.ylabel("Happy Score");
plt.scatter(data["avg_income"],data["happyScore"],s = ineq*10,alpha = 0.25,color = "crimson");
for k,row in richest.iterrows():
    plt.text(row["avg_income"],row["happyScore"],row["country"])
    print(row["country"])
plt.show();

# plt.show();
income = data["avg_income"];
happy = data["happyScore"];
income_happy = np.column_stack((income,happy))
# print(income_happy);

km_res = KMeans(n_clusters=6).fit(income_happy);
print(km_res);
print(km_res.cluster_centers_);
clusters = km_res.cluster_centers_;
plt.scatter(income,happy);
plt.scatter(clusters[:,0],clusters[:,1],s =1000,alpha =0.5);
plt.show();
