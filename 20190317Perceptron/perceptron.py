import numpy as np
import matplotlib.pyplot as plt
import plotFig as plf

plf.figDefault(figSize=[7, 6], lineLw=0.5, lineMew=0.5, lineMS=2.0, axLw=0.5,
               axLs=8, tickLs=6, lgFs=8, colorOrder=None)

class perceptron:
    def __init__(self, x, y, nsample_loc='first', **kwargs):
        if nsample_loc.lower() == 'last':
            x = x.transpose()
        self.__x = x
        self.__y = y
        self.__data = zip(x, y)
        nfeature = x.shape[1]
        if 'lr' in kwargs.keys():
            self.__lr = kwargs['lr']
        else:
            self.__lr = 1
        if 'w0' in kwargs.keys():
            self.__w = kwargs['w0']
        else:
            self.__w = np.zeros(nfeature)
        if 'b0' in kwargs.keys():
            self.__b = kwargs['b0']
        else:
            self.__b = 0
        if 'margin' in kwargs.keys():
            self.__margin = kwargs['margin']
        else:
            self.__margin = 1e-6

    def plotData(self, disp=True):
        # Only able to plot 2D data.
        for idx in range(len(self.__y)):
            if self.__y[idx] > 0:
                plt.scatter(self.__x[idx, 0], self.__x[idx, 1], marker='o', color='r')
            else:
                plt.scatter(self.__x[idx, 0], self.__x[idx, 1], marker='o', color='b')
        if disp: plt.show()

    def train(self, epochs=20):
        for epoch in range(epochs):
            flag = 0
            for xi, yi in self.__data:
                if (xi.dot(self.__w) + self.__b) * yi <= 0:
                    self.__w = self.__w + self.__lr * xi * yi
                    self.__b = self.__b + self.__lr * yi
                    flag = 1
                self.__data = zip(self.__x, self.__y)
            if flag == 0: break
            if epoch == epochs and flag == 1: print("Cannot find separate line.")

        return self.__w, self.__b, epoch + 1

    def plotResult(self, disp=True):
        # Only able to plot 2D data.
        for idx in range(len(self.__y)):
            if self.__y[idx] > 0:
                plt.scatter(self.__x[idx, 0], self.__x[idx, 1], marker='o', color='r')
            else:
                plt.scatter(self.__x[idx, 0], self.__x[idx, 1], marker='o', color='b')
        y1 = self.__x[:, 1].min()
        y2 = self.__x[:, 1].max()
        x1 = - (self.__w[1] * y1 + self.__b) / (self.__w[0] + 1e-8)
        x2 = - (self.__w[1] * y2 + self.__b) / (self.__w[0] + 1e-8)
        # print(x1, y1)
        # print(x2, y2)
        plt.plot(np.array([x1, x2]), np.array([y1, y2]), 'k-')
        if disp: plt.show()


np.random.seed()
x = np.random.randn(96, 2) * 100
x[:, 1] = x[:, 1] * 2 +7
y = np.ones([96, 1])
for i in range(len(y)):
    if 5 * x[i, 0] + 2 * x[i, 1] - 9 < 0: y[i] = -1
a = perceptron(x, y, b0 = 900)
a.plotData()
w, b, epoch = a.train()
print(w, b, epoch)
a.plotResult()


