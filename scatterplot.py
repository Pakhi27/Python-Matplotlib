#  Scatter plot 
import matplotlib.pyplot as plt

day=[1,2,3,4,5,6,7]
no=[2,3,1,4,5,3,6]
no2=[3,4,5,6,7,8,9]
#  can passs numbers also instad of color - use color maps
# C=["r","y","r","g","r","y","g"]
C=[49,52,54,29,66,10,12]
sizes=[100,200,300,400,500,100,200]

plt.scatter(day,no,c=C,s=sizes,marker="*",edgecolor="g",linewidth=3,cmap="viridis")
plt.scatter(day,no2,c=C,s=sizes,marker="*",edgecolor="g",linewidth=3,cmap="viridis")
#  to check which color lies in which range
t=plt.colorbar()
t.set_label("ColorBar",fontsize=15)

plt.title("Scatter plot",fontsize=20)
plt.xlabel("Day",fontsize=15)
plt.ylabel("Number",fontsize=15)
plt.show()
