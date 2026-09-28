import pandas as pd

# print(pd.__version__)

# data = [100, 10 ,40 ,104, 200 ,99]

# series = pd.Series(data, index=["a" , "b" , "c","d" , "e" , "f"])
# series.loc["b"] = 30
# series.iloc[1]= 25
# print(series.loc["c"])
# print(series.loc["b"] ,"=",series.iloc[1])
# print(series)
# print(series[series >=100])

# calories = {
#   "Day 1" : 1750,
#   "Day 2" : 1650,
#   "Day 3" : 2150,

# }

# series =  pd.Series(calories)
# series.loc["Day 3"] -=150
# print(series.iloc[1], "=",series.loc["Day 2"])
# print(series[series>=2000])

employee = {
  "Name" : ["Berk" , "Emre" , "Ahmet"],
  "Age" : [28,28,34]
}
dataframe = pd.DataFrame(employee , index=["employee 1" , "employee 2",  "employee 3"])
dataframe["Job"]= ["Yazilim", "N/A",  "Cook"]
new_Rows = pd.DataFrame([{"Name" : "Selda",  "Age": 44 , "Job" :"HouseCaring"},
                        {"Name" : "Nehir",  "Age": 19 , "Job" :"Student"} ], index=["employee 4","employee 5"])
dataframe =pd.concat([dataframe , new_Rows])
print(dataframe)
# print(dataframe.loc["employee 1"], "\n", dataframe.iloc[0])