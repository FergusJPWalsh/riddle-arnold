import re
with open ("riddle-arnold.tsv", "r", encoding="utf-8") as f:
    # proper_names = csv.reader(f, delimiter="\t")
    proper_names = f.readlines()
    for i, entry in enumerate(proper_names):
        tabs = entry.count("\t")
        if tabs == 0:
            print(i+1)
        elif tabs > 1:
            print(i+1)
