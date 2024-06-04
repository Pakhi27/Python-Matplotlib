# step-plot- used in communications in signal
import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[2,4,6,8,10]

plt.step(x,y,marker="o",color="r",ms=10,mfc="g",label="python")
plt.title("Python")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend(loc=2)
plt.grid()
plt.show()

