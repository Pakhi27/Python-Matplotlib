#  subplots
import matplotlib.pyplot as plt
import numpy as np

x=[1,2,3,4]
y=[1,2,3,4]

plt.subplot(2,2,1)
plt.plot(x,y,color="r")

plt.subplot(2,2,2)
plt.pie([1],colors="r")

plt.subplot(2,2,3)
x1=[10,20,30,40]
plt.pie(x)

plt.subplot(2,2,4)
x2=["a","s","d","f"]
y2=[10,20,30,40]
plt.bar(x2,y2)

plt.show()