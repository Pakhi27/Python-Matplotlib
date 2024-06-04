#  histogram
import matplotlib.pyplot as plt
import numpy as np
import random

# x=np.random.randint(10,60,(50))
# print(x)
no=[30,26,31 ,10 ,35, 27, 59, 49, 26 ,38 ,28, 56, 18, 17 ,10, 52 ,42, 58, 51 ,50 ,11, 33 ,37, 56, 23 ,43, 44 ,45 ,19 ,39 ,56 ,53, 58 ,55 ,51, 47, 43 ,30 ,13 ,39, 43, 40, 42, 54 ,46, 27 ,36, 51, 18, 27]
l=[10,20,30,40,50,60]
plt.hist(no,"auto",(0,100),edgecolor="b",color="r",cumulative=-1,bottom=10,align="left",histtype="step",orientation="horizontal",rwidth=0.8,log=True,label="Python")
plt.title("histogram")
plt.xlabel("python")
plt.ylabel("number")

plt.legend()
plt.axvline(45,color="g",label="line")
plt.grid()
plt.show()