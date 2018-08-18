import matplotlib.pyplot as plt
import numpy as np


def cosplot():
    x = np.linspace(1, 10, 100)
    for i in range(7):
        plt.plot(x, np.cos(x + i * .5) * (7 - i))


# 使用sns设置之后的图形
cosplot()
plt.show()
