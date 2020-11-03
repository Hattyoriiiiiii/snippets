# 散布図(scatter)
import matplotlib.pyplot as plt
import numpy as np

X = [np.random.rand(100) * 10]
Y = [np.random.rand(100) * 10]

# 散布図を描画する
plt.scatter(X, Y)
plt.show()