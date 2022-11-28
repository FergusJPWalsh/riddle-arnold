import pandas as pd
import re

data = pd.read_csv("proofing/LewisShortauthorsworks.txt", delimiter="\t", header=None)
data = data.drop([1,2,3,4,5],axis=1)
pattern = re.escape("<b>")
data["match"] = data[0].str.match(pattern)
data = data[data["match"] == True]
print(data.head())

data[0] = data[0].str.replace(r"<[^<>]*>", "", regex=True)
data.dropna(subset=[0])

authors = data[0].to_list()

with open("author_names.txt", "w", encoding="utf-8") as f:
    for author in authors:
        f.write(f"{author}\n")