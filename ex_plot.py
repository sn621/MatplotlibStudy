import matplotlib.pyplot as plt
import pickle as pkl
import numpy as np
with open('sample_fx.pickle', mode='rb') as f:
     data = pkl.load(f)

# ex 2.1
fig1=plt.figure()
plt.plot(data[0],data[1],'o',ms=5)

# ex 2.2
fig2=plt.figure()
dict = {'xx':[0,2],'yy':[3,4]}
plt.plot('xx','yy',data=dict)

plt.show()
