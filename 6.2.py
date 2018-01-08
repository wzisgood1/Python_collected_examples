# Pandas package
import pandas as pd 

# brics = pd.read_csv("C:/Users/WangZhe/brics.csv")
brics = pd.read_csv("C:/Users/WangZhe/brics.csv", index_col = 0)

# choose and create columns and rows
brics["country"]
brics.country

brics["in_asia"] = [False, True, True, True, False]
brics["density"] = brics["population"] / brics["area"] * 1000000
# print(brics)

# choose columns as DataFrame
print(brics["country"])
print(brics[["area", "country"]])

# row access
brics.loc["BR"]

brics.loc["CH", "capital"]
brics["capital"].loc["CH"]
brics.loc["CH"]["capital"]
print(brics.capital.loc["CH"])

# choose rows as DataFrame
# print(brics.loc["BR"])
print(brics.loc[["CH", "BR"]])

# choose sub-DataFrame
print(brics[["area", "country"]].loc[["CH", "BR"]])