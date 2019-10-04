import matplotlib.pyplot as plt
import pickle as pkl
import numpy as np
with open('sample_coulomb.pickle', mode='rb') as f:
     data = pkl.load(f)

# ex 5.1
fig1=plt.figure()

lvs_tmp = -np.power(10.0,np.arange(-3,3+1e-9,1/10.0))[::-1]
lvs_tmp = np.append(lvs_tmp,np.array([0]))
lvs = np.append(lvs_tmp,np.power(10.0,np.arange(-3,3+1e-9,1/10.0)))
#plt.contour(data[0],data[1],data[2][0]+data[2][1]-data[2][2],levels=lvs)
plt.pcolormesh(data[0],data[1],data[2][0]+data[2][1]-data[2][2])
plt.show()
