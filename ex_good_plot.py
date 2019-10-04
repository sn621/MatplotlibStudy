import matplotlib.pyplot as plt
import pickle as pkl
import numpy as np
with open('sample_fx.pickle', mode='rb') as f:
     data = pkl.load(f)

with open('sample_noise.pickle', mode='rb') as f:
     data_n = pkl.load(f)

import ex_apperence

# ex 2.1
fig=plt.figure()
#plt.xkcd()
ax_up = plt.axes([0.15,0.41,0.6,0.5])
ax_up.plot(data[0],data[1],'--',ms=5)
ax_up.plot(data[0],data_n,'.',ms=5)
ax_up.tick_params(direction='in',bottom=True,labelbottom=False)
ax_up.set_ylabel('length [m]')

ax_low = plt.axes([0.15,0.1,0.6,0.29])
ax_low.plot(data[0],data[1]-data_n,'.',ms=5)
ax_low.set_xlabel('Time [s]')
ax_low.set_ylabel('residual [m]')
ax_low.set_ylim(-0.5-0.005,0.5+0.005)
ax_low.tick_params(direction='in',right=True)


ax_right = plt.axes([0.76,0.1,0.2,0.29])
ax_right.hist(data[1]-data_n,orientation='horizontal',histtype='step',bins=np.arange(-0.1,0.1001,0.01))
ax_right.set_xlabel('Entries')
ax_right.set_ylim(-0.5-0.005,0.5+0.005)

ax_right.tick_params(direction='in',bottom=True,labelleft=False)

#ax_right.set_ylabel('Entries')

plt.show()
