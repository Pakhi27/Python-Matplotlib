import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[2,4,3,6,4]

plt.plot(x,y,color="r")

#  line is figure name
plt.savefig("Line")

#  dpi for clarity even after zooming
plt.savefig("Line1",dpi=2000)

#  border=green transparent takes true or false,box inches
plt.savefig("Line2",dpi=2000,facecolor="g",transparent=True,box_inches="tight")

# to save figure as pdf
plt.savefig("Line12.pdf",dpi=2000)
plt.show()