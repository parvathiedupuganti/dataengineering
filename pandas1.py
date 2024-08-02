import pandas as pd
import numpy as np
df = pd.read_csv("income.csv")# reading the csv files using pandas
#print(df)
#income_dc = df.columns # all data columns from the income data set
#print(income_dc)
#print(income_dc[:2])
#print(df.dtypes)
#df.Y2008 = df.Y2008.astype(float)
#print(df.dtypes)
#print("total nuber of rows and columns:",df.shape)
#print("total nuber of rows:",df.shape[0])
#print("total nuber of columns:",df.shape[1])
#print(df.head())  #gives 1st 5 records
#print(df.tail())  #gives last 5 records
#print(df.head(10)) #gives 1st 10 records
#print(df.tail(10)) #gives last 10 records
#print(df.iloc[5:10]) # 
#print(df[0:5])
# print("distinct values of column index")
# u_values = df.index.unique()
# print(u_values, len(u_values))
# print(df.head()) 
#biverate frequency distribution
print(pd.crosstab(df.Index,df.State))
 
#creating frequency distribution based on the Index
#print(df.Index.value_counts(ascending=True))
 
#Random Sampling
#data = df.sample(n=10) #getting 10 rows as sample from entire dataset
#print(data)
# data = df.sample(frac=0.1) #sample of 10% of the entire dataset
# print(data)
#print(data["State"] , data.State) #selecting columns
# difference of 2 columns
# df["difference"] = df.Y2008 - df.Y2009
# print(df["difference"])
# other way 2 find difference
#df["difference2"] = df.eval("Y2003 - Y2002")
#print(df["difference2"])
#other way to find diffrence
# data = df.assign(ratio = (df.Y2008/df.Y2009))
# print(data.head())
#print(df.describe())  # function is used to generate descriptive statistics of a DataFrame 
#print(df.describe(include=['object']))
#print(df.Y2008.mean(),df.Y2008.median(),df.Y2008.agg(["mean","median"]))
#print(df.Year2008.min())
#print(df.Year2008.agg(["mean","median","min"]))

""" Group By Functions """
# result = df.groupby("Index")[["Y2002","Y2003"]].min()
# print(result)

# result1= df.groupby("Index")[["Y2002","Y2003"]].agg(["min","max","mean"])
# print(result1)

# print(df.groupby("Index").agg({"Y2002":[min,max],"Y2003": "mean"}))

# dt = df.groupby("Index").agg({"Y2002":[min,max],"Y2003": "mean"})
# dt.columns = ['Y2002_min', 'Y2022_max', 'Y2003_mean']
# print(dt)

# print(df.groupby(["Index","State"]).agg({"Y2002":[min,max],"Y2003": "mean"}))

""" Filtering """
# print(df[df.Index=="A"])
# print(df.loc[df.Index=="A"])#All the columns where Index is A
#print(df.loc[df.Index=="A","State"])# only State Column where Index is A

#filter the rows with index as A and salary greater than 15 lacs
#print(df.loc[(df.Index=="A") & (df.Y2002 > 1500000),:])

#filter the  rows with index either A or W
#print(df.loc[(df.Index=="A") | (df.Index=="W"),:])
##alternative
# print(df.loc[df.Index.isin(["A","W"]),:])

#alternative
# print(df.query("Y2002>1700000 & Y2003>1500000"))


























