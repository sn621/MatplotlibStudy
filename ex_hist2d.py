import matplotlib.pyplot as plt
import pickle as pkl
import numpy as np
with open('sample_gauss.pickle', mode='rb') as f:
     data = pkl.load(f)

# bin configuration
bincfg = np.arange(-5,5,0.5)

# ex 4.1
fig1=plt.figure()

weight_for_norm = np.ones(len(data[0]))/(len(data[0]))
from matplotlib.colors import LogNorm
H = plt.hist2d(data[0],data[1],bins=[bincfg,bincfg],weights=weight_for_norm,norm=LogNorm(),cmap='plasma')
#H[3].set_clim(1e-5,1e-2)
plt.colorbar(H[3])

plt.show()
