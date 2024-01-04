import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

music_data=pd.read_csv('music.csv')

# print(music_data.shape)

X=music_data.drop(columns=['genre'])
Y=music_data['genre']

model=DecisionTreeClassifier()
model.fit(X,Y)

predictions=model.predict([[21,1],[22,0]])

# print(predictions)

tree.export_graphviz(model,out_file='music-recommender.dot', feature_names=['age','gender'],class_names=sorted(Y.unique()),
                     label='all',rounded=True,filled=True)