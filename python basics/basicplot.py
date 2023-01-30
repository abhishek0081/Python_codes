import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
# import time
# x = [12,6,7,34,5,7,56];
# y = [8,-3,6,7,4,-6,0];
# plt.scatter(x,y);
# plt.show();
# nx = [[10,123],[55,78],[90,67],[46,90],[34,89],[78,90]];
# nx = np.array(nx);
# print(nx);

# print(nx[:,0],nx[:,-1]);
# plt.show();
nx1 = [[10,125],[100,26],[25,66],[67,1],[74,10]];
nx1 = np.array(nx1);
# plt.scatter(nx1[:,0],nx1[:,1]);
# plt.show();
##########  multidimensional mean ###########
X_mean = np.mean(nx1[:,0]);
#
Y_mean = np.mean(nx1[:,1]);
print(nx1,np.mean(X_mean),np.mean(Y_mean),np.mean(nx1,0));## colu,n wise mean
mean = np.mean(nx1,0);
# fig, (ax1, ax2) = plt.subplots(1,2, figsize=(10,5));
std_dev = np.std(nx1,0);
ellipse = patches.Ellipse([mean[0],mean[1]],std_dev[0]*2,std_dev[1]*2,alpha =0.25);
fig,graph=plt.subplots();
graph.scatter(nx1[:,0],nx1[:,1]);
graph.scatter(mean[0],mean[1]);

graph.add_patch(ellipse);

# plt.show();
# for i in range(0,4):
#     x = np.linalg.norm(nx1[i]-mean);
#     # print(x);


# x = [np.linalg.norm(nx1[i]-mean) for i in range(0,4) ]
# # print(x);
# z = lambda x: [np.linalg.norm(nx1[i]-mean) for i in range(0,4) ];
# print(z(nx1));

nx_min = np.min(nx1,0);
nx_max = np.max(nx1,0);
print(nx_min,nx_max);
normed_x = (nx1-nx_min)/(nx_max-nx_min);
print(normed_x);
print(nx1);
mean = np.mean(normed_x,0);
std_dev = np.std(normed_x,0);
ellipse = patches.Ellipse([mean[0],mean[1]],std_dev[0]*2,std_dev[1]*2,alpha =0.25);
fig,graph=plt.subplots();
graph.scatter(normed_x[:,0],normed_x[:,1]);
graph.scatter(mean[0],mean[1]);

graph.add_patch(ellipse);
plt.show();