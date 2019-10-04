import matplotlib.pyplot as plt
import pickle as pkl
import numpy as np
data = []
with open('sample_scatter.pickle', mode='rb') as f:
     data.append(pkl.load(f))

with open('sample_gauss.pickle', mode='rb') as f:
     data.append(pkl.load(f))

# ex 3.1
fig1=plt.figure()
plt.scatter(data[0][0],data[0][1],s=np.ones(len(data[0][0])))
plt.scatter(data[1][0]+4,data[1][1]+4,s=np.ones(len(data[0][0])))

# ex 3.2
fig1=plt.figure()
plt.scatter(data[1][0],data[1][1],s=(data[1][1]**2+data[1][0]**2),c=(data[1][1]**2+data[1][0]**2),cmap='jet')
plt.show()
