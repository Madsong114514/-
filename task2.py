import numpy as np
import matplotlib.pyplot as plt
np.random.seed(189)
array=np.random.normal(5,0.2,100)
plt.hist(array,bins=20) 
plt.title('X=188')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True,alpha=0.3)
plt.show()
