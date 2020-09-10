import matplotlib.pyplot as plt
import numpy as np

#create period
x = np.linspace(0,2*np.pi,1000,endpoint=True)
cosine, sine, tangent = np.cos(x), np.sin(x), np.tan(x)

#plot sine and cosine
plt.plot(x, sine, color = 'darkblue', label = 'Sine')
plt.plot(x, cosine, color = 'darkred', label = 'Cosine')
plt.plot(x, tangent, color = 'darkgreen', label = 'Tangent')

#indicate dimensions and tick names, customize plot
plt.xlim(0, 2 * np.pi)
plt.ylim(-2,2)
plt.xticks([0, np.pi/2, np.pi, 3 * np.pi/2, 2*np.pi],[r'$0$', r'$+\pi/2$', r'$+\pi$', r'$+3\pi/2$', r'$+2\pi$'])
plt.yticks([-2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2])
plt.title("Sine, Cosine and Tangent Curves")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True, which = 'both')

ax=plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')#17
ax.spines['left'].set_position(('data',0))
plt.legend(loc='lower left')
plt.show()
