import pandas as pd
wdata=pd.read_csv('netflix_titles.csv')
#print(type(wdata))
#print(wdata.head(8))
#print(wdata.tail(10))
#print(wdata.shape)
#print(wdata.index)
#print(wdata.iloc[0:5,0:3])
#print(wdata.columns)
#print(wdata.dtypes)
#print(wdata.unique())
#print(wdata.title.unique())
#print(wdata.title.nunique())
#print(wdata.count())
#print(wdata.value_counts())
#print(wdata.title.value_counts())
#print(wdata.info())
print(wdata.release_year--2018)
#print(wdata.[wdata.release_year--2018])
print(wdata.groupby('release_year').get_group(2018))





