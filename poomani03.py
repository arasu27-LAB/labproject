import pandas as pd
#Reading the csv file
df=pd.read_csv(r'C:\happylife.csv')
#Printing top 5 rows
df.head()
df.shape
df.info()
df.describe()
df.isnull().sum()
data=df.drop_duplicates(subset="Species",)
data
df.value_counts("Species")

#impoting packages
import seaborn as sns
import matplotlib.pyplot as plt
sns.countplot(x='Species',data=df,)
plt.show()

#importing packages
import seaborn as sns
import matplotlib.pyplot as plt
sns.scatterplot(x='SepalLengthCm',y='SepalWidthCm',hue='Species',data=df,)
#Placing Legend outsidethe Figure
plt.legend(bbox_to_anchor=(1,1),loc=2)
plt.show()

#importing packages
import seaborn as sns
import matplotlib.pyplot as plt
sns.pairplot(df.drop(['Id'],axis=1),hue='Species',height=2)

#importing packages
import seaborn as sns
import matplotlib.pyplot as plt
fig,axes=plt.subplots(2,2,figsize=(10,10))
axes[0,0].set_title("Sepal Length")
axes[0,0].hist(df['SepalLengthCm'],bins=7)
axes[0,1].set_title("Sepal Width")
axes[0,1].hist(df['SepalWidthCm'],bins=5)
axes[1,0].set_title("Petal Length")
axes[1,0].hist(df['PetalLengthCm'],bins=6)
axes[1,1].set_title("Petal Width")
axes[1,1].hist(df['PetalWidthCm'],bins=6)

#importing packages
import seaborn as sns
import matplotlib.pyplot as plt
plot=sns.FacetGrid(df,hue="Species")
plot.map(sns.distplot,["SepalLengthCm"]).add_legend()
plot=sns.FacetGrid(df,hue="Species")
plot.map(sns.distplot,["SepalWidthCm"]).add_legend()
plot=sns.FacetGrid(df,hue="Species")
plot.map(sns.distplot,["PetalLengthCm"]).add_legend()
plot=sns.FacetGrid(df,hue="Species")
plot.map(sns.distplot,["PetalWidthCm"]).add_legend()
plt.show()

