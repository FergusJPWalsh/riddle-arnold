# import csv
bad_entries = 0
with open ("riddle-arnold.tsv", "r", encoding="utf-8") as f:
    # proper_names = csv.reader(f, delimiter="\t")
    proper_names = f.readlines()
    for i, entry in enumerate(proper_names):
        tabs = entry.count("\t")
        if tabs != 1:
            bad_entries = bad_entries + 1
            print(i+1,entry)
            print(bad_entries)