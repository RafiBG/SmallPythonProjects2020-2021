import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axisartist import SubplotZero


class Axes():

    def __init__(self, xlim=(-5, 5), ylim=(-5, 5), figsize=(12, 5)):
        self.xlim = xlim
        self.ylim = ylim
        self.figsize = figsize
        self.__scale_arrows__()

    def __drawArrow__(self, x, y, dx, dy, width, length):
        plt.arrow(
            x, y, dx, dy,
            color='k',
            clip_on=False,
            head_width=self.head_width,
            head_length=self.head_length
        )

    def __scale_arrows__(self):
        xrange = self.xlim[1] - self.xlim[0]
        yrange = self.ylim[1] - self.ylim[0]

        self.head_width = min(xrange / 30, 0.25)
        self.head_length = min(yrange / 30, 0.3)

    def __drawAxis__(self):

        ax = SubplotZero(self.fig, 1, 1, 1)
        self.fig.add_subplot(ax)

        for axis in ["xzero", "yzero"]:
            ax.axis[axis].set_visible(True)
        for n in ["left", "right", "bottom", "top"]:
            ax.axis[n].set_visible(False)

        plt.xlim(self.xlim)
        plt.ylim(self.ylim)

        self.__drawArrow__(self.xlim[1], 0, 0.01, 0, 0.3, 0.2)  # x-axis arrow
        self.__drawArrow__(0, self.ylim[1], 0, 0.01, 0.2, 0.3)  # y-axis arrow

    def draw(self):
        self.fig = plt.figure(figsize=self.figsize)
        self.__drawAxis__()


axes = Axes(xlim=(-100, 100), ylim=(-100, 100), figsize=(9, 7))
axes.draw()
x = np.arange(-100, 101, 1)
y = 6 + x*0
plt.plot(x, y)
plt.show()
