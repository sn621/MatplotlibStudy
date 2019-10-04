import matplotlib.pyplot as plt
import pickle as pkl
import numpy as np
with open('sample_gauss.pickle', mode='rb') as f:
     data = pkl.load(f)

# bin configuration
bincfg = np.arange(-5,5,0.5)

# ex 1.1
fig1=plt.figure()
plt.hist(data,bins=bincfg,histtype='bar',rwidth=0.5)
plt.title('Side by side')

# ex 1.2
fig2=plt.figure()
plt.hist(data,bins=bincfg,histtype='barstacked',stacked=True)
plt.title('Stacked hist')

# ex 1.3
fig3=plt.figure()
plt.hist(data[0],bins=bincfg,histtype='step',weights=np.ones(len(data[0]))/len(data[0]))
plt.hist(data[0],bins=bincfg,histtype='step',density=True)
plt.title('Normalization comparison')
plt.show()
