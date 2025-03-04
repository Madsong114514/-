import numpy as np
import matplotlib.pyplot as plt

np.random.seed(189)
n = [2,4,8,16,32,64,128,256,512,1024,2000,2048,3000,3500,4096,5000,5500,9000]
coins = [np.random.binomial(ni, 0.5,1)/ni for ni in n] 

plt.figure(figsize=(10, 6))
plt.scatter(n, coins)
plt.xlabel('Number of coin flips')
plt.ylabel('Number of heads')
plt.grid(True, alpha=0.3)
plt.show()