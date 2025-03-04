import pandas as pd
df=pd.read_csv("heart.csv")
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
#print(df.isnull().sum().plot_bar)
#df=df.fillna(0)
df=df.dropna()
print(df.info)
print(df.isnull().sum())
print(df["ChestPain"].value_counts())
print(df.loc[[100,101],["ChestPain","Sex","AHD"]])
print(df.iloc[2,:])
print(df.iloc[:,[1,2]])
df=df.drop("index",axis=1)

from sklearn.preprocessing import LabelEncoder
Le=LabelEncoder()
df["ChestPain"]=Le.fit_transform(df["ChestPain"])
df["AHD"]=Le.fit_transform(df["AHD"])
df["Thal"]=Le.fit_transform(df["Thal"])
print(df.info())
x=df.iloc[:,:-1].values
y=df.iloc[:,-1].values
print(x.shape)
print(y.shape)
from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,random_state=10)
print(xtrain.shape)
print(xtest.shape)
print(ytrain.shape)
print(ytest.shape)
from sklearn.neighbors import KNeighborsClassifier
classifier=KNeighborsClassifier(n_neighbors=13)
classifier.fit(xtrain,ytrain)
print(classifier)
out=classifier.predict(xtest)
print(out)
from sklearn.metrics import accuracy_score
acc=accuracy_score(ytest,out)
print(acc)
xnew=[[63,1,2,145,233,1,2,150,0,2.3,3,0,1]]
output=classifier.predict(xnew)
print(output)






