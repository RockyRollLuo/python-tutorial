from DeepLearning_Maizi.indi.maizi.NerualNetworks.NeuralNetwork import NeuralNetwork

import numpy as np

nn = NeuralNetwork([2,20,1],"tanh")
x= np.array([[0,0],[0,1],[1,0],[1,1]])
y= np.array([0,1,1,0])
nn.fit(x, y)

print("开始预测")
for i in [[0,0],[0,1],[1,0],[1,1]]:
    print(i,nn.predict(i))
    