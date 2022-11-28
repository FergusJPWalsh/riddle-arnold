import re
with open("author_names.txt", "r", encoding="utf-8") as f:
    authors = f.readlines()
    authors = " ".join(authors)

if re.search(r"Cic.", authors):
    print("match!")