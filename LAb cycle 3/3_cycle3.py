import pandas as pd
from matplotlib import pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import numpy as np

data = pd.read_csv('Iris.csv')
df = pd.DataFrame(data)

# def bar_species():
#     sp_ls = data['Species'].value_counts()
#     sp_ls.plot(kind = "bar",color = ['r','g','b'], xlabel = 'frequency', ylabel = 'species')
#     plt.title("Bar Chart")
#     plt.show()

# bar_species()

#def principle_component_distribution():
#Removing species column
x  = data.iloc[:,:-1]
x = StandardScaler().fit_transform(x) #normalising the data

# PCA to get 2 components
from sklearn.decomposition import PCA
pca =  PCA(n_components=2)
print(pca)
pc_iris = pca.fit_transform(x)
#print(pc_iris)
#forming data frame with PCA Values
principalDF = pd.DataFrame(data=pc_iris,
    columns = ['principal component 1','principal component 2'])
principalDF.tail()
#print(principalDF)

plt.figure()
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
targets = ['Iris-setosa','Iris-versicolor','Iris-virginica']
colors = ['r','g','b']
for target,color in  zip(targets,colors):
    indices_to_Keep = data['Species'] == target
    plt.scatter(principalDF.loc[indices_to_Keep,'principal component 1'],
    principalDF.loc[indices_to_Keep,"principal component 2"],c = color)
    plt.show()


def histogram(name,hcolor,title,x):
    data[name].hist(color=hcolor)
    plt.xlabel(x)
    plt.ylabel('frequency')
    plt.title(title)
    plt.show()

histogram('SepalLengthCm','b',"Histogram-Sepal Length",'Sepal Length cm')
histogram('PetalLengthCm','r',"Histogram-Petal Length",'Petal Length cm')
histogram('SepalWidthCm','g',"Histogram-Sepal Width",'Sepal Width cm')
histogram('PetalWidthCm','yellow',"Histogram-Petal Width",'Petal Width cm')

