import matplotlib.pyplot as plt

# x=[10,20,30,40]
# y=["c","c++","java","python"]
# ex=[0.3,0.0,0.0,0.0]
# C=["r","b","m","y"]
# plt.pie(x,labels=y,explode=ex,colors=C,autopct="%0.1f%%",shadow=True,radius=1,labeldistance=1.2,startangle=0,textprops={"fontsize":15},counterclock=True,wedgeprops={"linewidth":5,"width":2,"edgecolor":"g"},center=(1,3),rotatelabels=True)
# plt.title("My pie chart")
# plt.legend(loc=2)
# plt.show()

# Dot pie chart
# plt.pie([1])
# plt.show()

# Donat pie  chart
# x=[10,20,30,40]
# y=["c","c++","java","python"]

# x1=[40,30,20,10]

# plt.pie(x,labels=y,radius=1.5)
# plt.pie(x1,radius=1)

# plt.show()
#  ring pie chart
x=[10,20,30,40]
y=["c","c++","java","python"]

x1=[40,30,20,10]

plt.pie(x,labels=y,radius=1.5)
# plt.pie([1],colors="w")
#  another method to make ring pie chart
cr=plt.Circle(xy=(0,0),radius=1,facecolor="w")
plt.gca().add_artist(cr)

plt.show()
