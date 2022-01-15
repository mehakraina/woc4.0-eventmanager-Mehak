import numpy as np

data=np.genfromtxt('file.txt',delimiter=';')
data=data.astype('int32')

num=data>40
num=data[num]
print(num)
