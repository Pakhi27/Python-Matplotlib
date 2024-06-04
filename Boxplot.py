import matplotlib.pyplot as plt

x=[10,20,30,40,50,60,70,120,200]

# # notch-to vhange the shape,patch_artist- to fill the color,whis to join the line with the outlier,outlier-for extra data,sym-to change the shape and color of outlier,cap=max and min line
plt.boxplot(x,notch=True,vert=False,widths=0.5,labels=["python"],patch_artist=True,showmeans=True,whis=3.5,sym="g+",boxprops=dict(color="r"),capprops=dict(color="g"),whiskerprops=dict(color="m"),filerprops=dict(markeredgecolor="y"))
plt.show()

#  for multiple box plots

x=[10,20,30,40,50,60,70,120]
x1=[10,20,40,50,70,80,90,130]

y=[x,x1]
plt.boxplot(y,notch=True,vert=True,widths=0.5,patch_artist=True,showmeans=True,whis=3.5,sym="g+",boxprops=dict(color="r"),capprops=dict(color="g"),whiskerprops=dict(color="m"),flierprops=dict(markeredgecolor="y"),labels=["python","c++"])
# plt.boxplot(x1,notch=True,vert=True,widths=0.5,patch_artist=True,showmeans=True,whis=3.5,sym="g+",boxprops=dict(color="r"),capprops=dict(color="g"),whiskerprops=dict(color="m"),flierprops=dict(markeredgecolor="y"))
plt.show()