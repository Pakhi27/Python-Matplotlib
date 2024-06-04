# bar plot
import matplotlib.pyplot as plt
import numpy as np

x=["python","c","c++","java"]
y=[85,70,60,80]
z=[20,30,40,50]

plt.xlabel("languages",fontsize=15)
plt.ylabel("number",fontsize=15)
plt.title("Analysis",fontsize=15)

C=["y","b","r","g"]
#  edge or center by default center aligned alpha for maling it blur ranges from 0 to 1
plt.bar(x,y,width=0.4,color="r",align="edge",edgecolor="r",linewidth=5,alpha=0.4,label="Popularity")
plt.bar(x,z,width=0.4,color="y",align="edge",edgecolor="r",linewidth=5,alpha=0.4,label="Popularity1")

plt.legend()
plt.show()

# to shift second graph from first one

X=["python","c","c++","java"]
Y=[85,70,60,80]
Z=[20,30,40,50]

width=0.35
# # shift=width/3
P=np.arange(len(X))
P1=[j+width for j in P]

plt.xlabel("languages",fontsize=15)
plt.ylabel("number",fontsize=15)
plt.title("Analysis",fontsize=15)

# # C=["y","b","r","g"]
# #  edge or center by default center aligned alpha for maling it blur ranges from 0 to 1
plt.bar(P,Y,color="r",align="edge",edgecolor="r",linewidth=5,linestyle=":",alpha=0.4,label="Popularity",width=0.4)
plt.bar(P1,Z,color="y",align="edge",edgecolor="r",linewidth=5,linestyle=":",alpha=0.4,label="Popularity1",width=0.4)
plt.xticks(P+width/1,X,rotation=10)
plt.legend()
plt.show()


# For horizontal bar graph
X=["python","c","c++","java"]
Y=[85,70,60,80]
Z=[20,30,40,50]


plt.xlabel("languages",fontsize=15)
plt.ylabel("number",fontsize=15)
plt.title("Analysis",fontsize=15)


plt.barh(X,Y,color="r",label="Popularity")
plt.barh(X,Z,color="y",label="Popularity1")

plt.legend()
plt.show()