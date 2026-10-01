import pandas as pd
import numpy as np

df = pd.read_csv("data.csv", index_col="Name")

# df=pd.read_json("data.json")
# df=pd.read_json("C:\\Users\\berke\\Desktop\\data.json")
# print(df.to_string())
# print(df["Name"])
# print(df["Height"])
# print(df["Weight"])

# print(df[["Name", "Height" , "Weight"]])

# print(df.loc["Charizard":"Pikachu",["Height","Weight"]])

# print(df.iloc[0:11:2,1:5])

# pokemon = input("Enter a Pokemon Name : ")


# try:
#   print(df.loc[pokemon])
# except KeyError:
#   print(f"{pokemon} not found")

# tall_pokemon = df[df["Height"]>=2]
# heavy_pokemon = df[df["Weight"]>=100]
# legandary_pokemon = df[df["Legendary"]==1]
# type_pokemon = df[(df["Type1"]=="Psychic") |
#                   (df["Type2"]=="Psychic") ]

# ff_pok = df[(df["Type1"]=="Fire") & (df["Type2"]=="Flying")]
# print(ff_pok[[ "No","Type1", "Type2"]])
# print(df)

# print(df.mean(numeric_only=True))
# print(df.sum(numeric_only=True))
# print(df.min(numeric_only=True))
# print(df.max(numeric_only=True))
# print(df.count())


# print(df["Height"].mean())
# print(df["Height"].sum())
# print(df["Height"].min())
# print(df["Height"].max())
# print(df["Height"].count())

# group = df.groupby("Type1")

# print(group["Height"].mean())
# print(group["Height"].sum())
# print(group["Height"].min(), group["Height"].max())
# print(group["Height"].count())

# df = df.drop(columns=["Legendary","No"])
# df =df.dropna(subset=["Type2"])
# print(df.to_string())
# df = df.set_index("Type1")
# df.reset_index()
# print(df["No"].is_unique )
# df["Type2"].fillna("---")
# df = df.fillna("None")
# print(df["Type2"].notna())
# df["Legendary"] = df["Legendary"].astype(bool)
# df[["Type1","Type2"]] = df[["Type1","Type2"]].astype("category")

# tipler = df[(df["Type1"] == "Poison") |
#               (df["Type2"] == "Poison")]
# print(tipler["No"].count())

# tipler = pd.concat([df["Type1"], df["Type2"]]).dropna()
# print(tipler.value_counts())
# poison_t =df[(df["Type1"] =="Poison")&
#             (df["Type2"]=="Flying")]
# print(poison_t)
# print(np.log1p(df["Weight"]))

# df.groupby("Type1")[["Height", "Weight"]].median()
# print(df.groupby("Type1")[["Height", "Weight"]].median())
# df.sort_values("Weight", ascending=False).head(10)
# print(df.sort_values("Weight", ascending=False).head(10))
# df["BMI"] = df["Weight"] / df["Height"]**2
# print(df[["Weight", "Height", "BMI"]].to_string())
# df["Type1"]= df["Type1"].replace({"Grass": "GRASS"})
# df= df.reset_index()
# df["Name"] = df["Name"].str.lower()
# df = df.drop_duplicates() #duplicates remove
print(df.to_string())
