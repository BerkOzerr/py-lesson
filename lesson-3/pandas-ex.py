import pandas as pd
import numpy as np
df = pd.read_csv("data.csv")
# print(df[:5])

# print(df.shape)

# print(df.columns)

# print(df[["Name", "Weight"]])

# print(df[df["Weight" ]>100])

# print(df[df["Type1"]=="Fire"])

# legendary_pokemon = df[df["Legendary"]==1]
# print(legendary_pokemon[["Name"]])

# print(df[(df["Type1"]=="Water")&
#         ( df["Type2"]=="Flying")])

# print(df["Weight"].mean())
# max_weig = df["Weight"].max()
# print(df[df["Weight"]==max_weig])
# max_heig = df["Height"].max()
# print(df[df["Height"]==max_heig])

# group = df.groupby(["Type1"]).count()
# print(group["Name"])

# group = df[df["Legendary"]==1].count()

# print(group["No"])

# mean_poke = df["Weight"].mean()

# print(df[df["Weight"]>mean_poke])

# typeFire = df[df["Type1"]=="Fire"]
# print(typeFire["Weight"].mean())

# group = df.groupby(["Type1"])
# print(group["Weight"].mean())

# firepoke, waterPoke=  df[df["Type1"] =="Fire"] , df[df["Type1"]=="Water"]

# print(firepoke["Weight"].mean() , "<- fire","water ->", waterPoke["Weight"].mean())

# print(
#   df[(df["Legendary"]==0 )&
#      (df["Weight"]>50 ) &
#      (df["Height"]>1.5 )]
# # )

# fiveWeight = df.sort_values("Weight").tail(5).iloc[::-1]
# print(fiveWeight[["Name", "Type1", "Weight"]])

# group = df.groupby("Type1").count()

# print(group["No"])
counts = df["Type1"].value_counts()
##############Önemli Öğren
print(counts)
print(counts.idxmax())

"""
value_counts()

→ Her değerin kaç kez geçtiğini bulur.

idxmax()

→ En büyük değerin bulunduğu index'i verir.
"""
# waterPoke= df[df["Type1"]=="Water"]
# waterPoke= waterPoke.sort_values("Height").tail(3)
# print(waterPoke)

# noLegPoke= df[df["Legendary"] ==False]
# legPoke = df[df["Legendary"] ==True]
##################Önemli
print(df.groupby("Legendary")["Weight"].mean())
# print(legPoke["Weight"].mean(), "<-noLegendary","legendary->",noLegPoke["Weight"].mean())
# ax = df[(df["Type1"] =="Fire") &
#      (df["Weight"] >20)]
# print(
#    ax["Name"]
# )

############################Önemli
print(df.loc[
    (df["Type1"] == "Fire") & (df["Weight"] > 20),
    "Name"
])

print(df.loc[
    (df["Type1"] == "Fire") & (df["Weight"] > 20) & (df["Height"] > 1.5),
      "Name"
])