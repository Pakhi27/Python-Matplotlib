import matplotlib.pyplot as plt

x=[1,2,3,4,5]
area=[1,2,3,5,4]
area1=[2,3,4,5,6]
area2=[1,2,3,5,4]

l=["area","area1","area2"]
plt.stackplot(x,area,area1,area2,labels=l,colors=["r","g","m"],baseline="zero")
plt.title("python")
plt.xlabel("x-ais")
plt.ylabel("y-axis")
# plt.grid()
plt.legend(loc=2)
plt.show()