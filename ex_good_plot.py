import matplotlib.pyplot as plt
import pickle as pkl
import numpy as np
with open('sample_fx.pickle', mode='rb') as f:
     data = pkl.load(f)

with open('sample_noise.pickle', mode='rb') as f:
     data_n = pkl.load(f)

import ex_apperence
from matplotlib.ticker import (MultipleLocator,FormatStrFormatter,AutoMinorLocator)

# ex 2.1
fig=plt.figure()
#plt.xkcd()
ax_up = plt.axes([0.15,0.41,0.8,0.5])
ax_up.tick_params(direction='in',bottom=True,labelbottom=False)

ax_up.plot(data[0],data[1],'--',label='pure function')
ax_up.plot(data[0],data_n,'.',label='Measurement')
ax_up.set_ylabel('length [m]')
ax_up.set_ylim(-1,1)
ax_up.xaxis.set_major_locator(MultipleLocator(2))
ax_up.xaxis.set_minor_locator(MultipleLocator(1))
ax_up.yaxis.set_major_locator(MultipleLocator(0.5))
ax_up.yaxis.set_minor_locator(MultipleLocator(0.1))

ax_low = plt.axes([0.15,0.1,0.8,0.29])
ax_low.tick_params(direction='in',top=True)

ax_low.plot(data[0],data[1]-data_n,'.')
ax_low.set_xlabel('Time [s]')
ax_low.set_ylabel('residual [m]')
ax_low.set_ylim(-0.5-0.005,0.5+0.005)
ax_low.xaxis.set_major_locator(MultipleLocator(2))
ax_low.xaxis.set_minor_locator(MultipleLocator(1))
#ax_low.yaxis.set_major_locator(MultipleLocator(0.25))
#ax_low.yaxis.set_minor_locator(MultipleLocator(0.05))


#ax_right = plt.axes([0.76,0.1,0.2,0.29])
#ax_right.hist(data[1]-data_n,orientation='horizontal',histtype='step',bins=np.arange(-0.1,0.1001,0.01))
#ax_right.set_xlabel('Entries')
#ax_right.set_ylim(-0.5-0.005,0.5+0.005)

#ax_right.tick_params(direction='in',bottom=True,labelleft=False)

#ax_right.set_ylabel('Entries')
ax_up.legend()
plt.show()
