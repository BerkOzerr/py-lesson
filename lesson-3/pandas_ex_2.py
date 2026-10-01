import pandas as pd
import numpy as np

# data = {
#     "name": ["Ali", "Ayşe", "Mehmet", "Zeynep"],
#     "age": [20, 22, 19, 21],
#     "math": [80, 65, 95, 75],
#     "english": [90, 70, 85, 95]
# }

# df = pd.DataFrame(data)
# # print(df["math"])
# print(df[df["math"] >80])
# print(df[["math","english"]].mean(axis=1))


# df = pd.DataFrame({
#     "isim": ["Ali", "Ayşe", "Mehmet", "Zeynep"],
#     "yas": [25, 32, 28, 41],
#     "sehir": ["Ankara", "İstanbul", "İzmir", "Bursa"],
#     "maas": [30000, 45000, 38000, 52000]
# })

# print(df.columns)
# print(df.iloc[2,:])

# print(df.loc[:,["isim", "maas"]])

# print(df.iloc[:3,2:])

# print(df.loc[df["yas"] >30 ,["isim"]])

# print(df.loc[df["maas"] >40000 ,["isim","sehir" , "maas"]])

# df = pd.DataFrame({
#     "isim": ["Ali", "Ayşe", "Mehmet", "Zeynep", "Can"],
#     "yas": [25, 32, 28, 41, 35],
#     "sehir": ["Ankara", "İstanbul", "İzmir", "Bursa", "Ankara"],
#     "maas": [30000, 45000, 38000, 52000, 47000]
# }, index=["A101", "A205", "A310", "A450", "A520"])

# print(df.loc[["A310"]])
# print(df.iloc[3,:])
# print(df.loc[["A205", "A450"]])

# print(df.loc[(df["yas"]>30) & (df["maas"]>45000) ,["isim" ,"maas"]])
# print(df.loc[(df["sehir"]=="Ankara") |
#              (df["sehir"]=="İzmir")])

# df = pd.DataFrame({
#     "isim": ["Ali", "Ayşe", "Mehmet", "Zeynep", "Can"],
#     "yas": [25, 32, 28, 41, 35],
#     "departman": ["IT", "HR", "IT", "Finance", "HR"],
#     "maas": [30000, 45000, 38000, 52000, 47000]
# })

# df.loc[df["departman"] =="IT" , ["maas"]] *= 1.15


# df.loc[df["yas"]<30 ,["departman"]]= "Junior"

# df.loc[df["maas"]>=50000 ,["maas"]] += 5000

# df["seviye"] ="Junior"

# df.loc[df["maas"]>=45000 ,["seviye"]]="senior"

# df.loc[(df["yas"]>30) &(df["maas"]<45000) ,["maas"]]  *= 1.10

# print(df)

# df = pd.DataFrame({
#     "isim": ["Ali", "Ayşe", "Mehmet", "Zeynep", "Can"],
#     "yas": [25, np.nan, 28, 41, np.nan],
#     "departman": ["IT", "HR", np.nan, "Finance", "HR"],
#     "maas": [30000, 45000, np.nan, 52000, 47000]
# })

# print(df.isna().sum())

# df.loc[df["yas"].isna(),["yas"]] = round(df["yas"].mean())

# df.loc[df["departman"].isna(),["departman"]]= "Unknown"

# df.loc[df["maas"].isna(),["maas"]] =40000

# df.loc[(df["yas"]>30)& (df["maas"].isna()),["maas"]] = 45000
# print(df)
