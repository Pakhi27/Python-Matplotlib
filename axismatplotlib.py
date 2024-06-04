import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[3,1,5,2,4]

plt.plot(x,y)

# to keep gap of 1 in x axis and y axis
plt.xticks(x,labels=["python","c","c++","java","sql"])
plt.yticks(y)

# limit in x axis and y axis
plt.xlim(0,10)
plt.ylim(0,10)

# limit in x axis and then limit in y axis
plt.axis([0,10,0,7])
plt.show()
