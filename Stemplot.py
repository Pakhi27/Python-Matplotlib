import matplotlib.pyplot as plt

x=[1,2,3,4,5,6]
y=[2,2,5,6,3,4]

plt.stem(x,y,linefmt=":",markerfmt="r+",bottom=1,basefmt="g",label="python",use_line_collection=False,orientation="horizontal")
plt.legend()
plt.show()